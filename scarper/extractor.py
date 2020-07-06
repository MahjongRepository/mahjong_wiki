# coding=utf-8
import os
import re

from lxml import etree
from slugify import slugify
import mistune
import subprocess


def main():
    skip_titles = [
        'Category:',
        'Category talk:',
        'Help talk:',
        'Help:',
        'Template talk:',
        'Template:',
        'MediaWiki talk:',
        'MediaWiki:',
        'File talk:',
        'File:',
        'Project:',
        'User talk:',
        'User:',
        'Talk:',
    ]

    current_directory = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(current_directory, 'arcturus/arcturussu_mjw.xml')

    pages = {}
    with open(xml_file, 'r') as f:
        root = etree.fromstring(f.read())

        for page_tag in root.findall('page', namespaces=root.nsmap):
            # skip system pages with redirects
            if page_tag.find('redirect', namespaces=root.nsmap) is not None:
                continue

            page = {}
            for child in page_tag:
                if etree.QName(child).localname == 'title':
                    page['title'] = child.text

                if etree.QName(child).localname == 'id':
                    page['id'] = child.text

                if etree.QName(child).localname == 'revision':
                    page['text'] = child.find('text', namespaces=root.nsmap).text

            if page and not any([page['title'].startswith(x) for x in skip_titles]):
                pages[page['title']] = page

    print('pages', len(pages.keys()))

    for key, page in pages.items()[1:]:
        slug = slugify(page['title'])
        wiki_file_path = os.path.join('%s.wiki' % slug)
        md_file_path = os.path.join('%s.md' % slug)
        final_md_file_path = os.path.join(current_directory, '..', 'hugo', 'content', 'english', 'riichi', 'wiki', os.path.join('%s.md' % slug))

        print(page['id'], slug, page['title'])

        with open(wiki_file_path, 'w') as f:
            content = page['text']
            content = process_kana_template(content)
            content = process_tiles_template(content)
            # ":{{<" happens for the start of tiles string
            content = content.replace(':{{<', '{{<')

            f.write(content.encode('utf-8'))

        subprocess.call([
            "docker", "run", "--rm", "--volume", '%s:/data' % current_directory,
            "pandoc/core:2.9.2.1",
            wiki_file_path,
            "-o", md_file_path,
            "-f", "mediawiki",
            "-t", "gfm",
            "--wrap", "preserve"
        ])

        # os.remove(wiki_file_path)
        os.rename(md_file_path, final_md_file_path)

        with open(final_md_file_path, 'r') as f:
            content = f.read()

        content = remove_escaping(content)

        with open(final_md_file_path, 'w') as f:
            # insert header
            f.seek(0, 0)
            f.write('+++\n')
            f.write('title = "%s"\n' % page['title'])
            f.write('id = "%s"\n' % page['id'])
            f.write('+++\n\n')

            f.write(content)

        break


def process_kana_template(content):
    """
    Replace mediawiki "kana" template http://arcturus.su/wiki/Template:Kana
    With our own shortcode.
    """
    regex = r"{{kana\|(.*?)}}"
    return re.sub(regex, r'{{< kana \1 >}}', content)


def process_tiles_template(content):
    """
    Replace mediawiki "mj" tiles extension
    With our own shortcode.
    """
    regex = r"{{#mjt:(.*?)}}"
    return re.sub(regex, r'{{< t \1 >}}', content)


def remove_escaping(content):
    """
    Pandoc escaped shortnames that we created before
    """
    content = content.replace('{{\<', '{{<')
    content = content.replace('\>}}', '>}}')
    return content


if __name__ == '__main__':
    main()
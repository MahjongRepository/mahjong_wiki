# coding=utf-8
import json
import os
import re
import subprocess

from slugify import slugify

current_directory = os.path.dirname(os.path.abspath(__file__))
export_dir = os.path.join(current_directory, 'arcturus', 'export')


def main():
    pages = os.listdir(export_dir)

    with open(os.path.join(export_dir, '_meta.json')) as f:
        meta_info = json.loads(f.read())

    for wiki_file_name in pages:
        if not wiki_file_name.endswith('.wiki'):
            continue

        meta = meta_info[wiki_file_name.split('.')[0]]

        # for debug
        # if meta['id'] != '261':
        #     continue

        print(meta['title'], meta['id'])
        wiki_content = load_and_prepare_wiki_file_content(wiki_file_name)
        title = meta['title']
        slug = slugify(title)
        temp_wiki_file_path = os.path.join('temp.wiki')

        with open(temp_wiki_file_path, 'w') as f:
            categories, wiki_content = preprocess_wiki_file_content(wiki_content)
            meta['categories'] = categories
            f.write(wiki_content)

        markdown_content, final_md_file_path = convert_to_markdown(slug)
        markdown_content = remove_escaping(markdown_content)

        with open(final_md_file_path, 'w') as f:
            markdown_content = process_wiki_links(markdown_content)
            markdown_content = remove_temp_tags(markdown_content)

            # insert header
            f.seek(0, 0)
            f.write('+++\n')
            f.write('title = "%s"\n' % title)
            f.write('id = "%s"\n' % meta['id'])
            f.write('categories = "%s"\n' % ", ".join(categories))
            f.write('+++\n\n')

            f.write(markdown_content)


def load_and_prepare_wiki_file_content(wiki_file_name):
    regex = r"{{#mjt:(.*?)}}"
    with open(os.path.join(export_dir, wiki_file_name), 'r') as f:
        lines = f.readlines()
        wiki_content = ''
        for line in lines:
            # it is important to remove starting spaces from line for future convertation to markdown format
            line = line.strip()

            # there were issues with parsing inherit tags,
            # to fix this we added this preprocessing
            if 'tilepattern =' in line.lower():
                line = re.sub(regex, r'{start-temp \1 end-temp}', line)

            if line.startswith('{{'):
                line = line.replace('{{Infobox', '{{infobox')

            if line.startswith(':{{#mjt'):
                line = line.replace(':{{#mjt', '{{#mjt')

            wiki_content += line
            wiki_content += '\n'

    return wiki_content


def preprocess_wiki_file_content(content):
    categories, content = process_categories(content)

    content = process_table_headers(content)
    content = process_infobox_blocks(content)
    content = process_kana_template(content)
    content = process_tiles_template(content)

    # let's just escape all unknown templates
    content = process_template_blocks(content)

    return categories, content


def convert_to_markdown(slug):
    final_md_file_path = os.path.join(
        current_directory, '..', 'hugo', 'content',
        'english', 'riichi', 'wiki', os.path.join('%s.md' % slug)
    )

    temp_wiki_file_path = 'temp.wiki'
    temp_md_file_path = 'temp.md'

    subprocess.call([
        "docker", "run", "--rm", "--volume", '%s:/data' % current_directory,
        "--user", "1000:1000",
        "pandoc/core:2.9.2.1",
        temp_wiki_file_path,
        "-o", temp_md_file_path,
        "-f", "mediawiki",
        "-t", "gfm",
        "--wrap", "preserve"
    ])

    os.remove(temp_wiki_file_path)
    os.rename(temp_md_file_path, final_md_file_path)

    with open(final_md_file_path, 'r') as f:
        return f.read(), final_md_file_path


def remove_temp_tags(content):
    regex = r"{start-temp(.*?)end-temp}"
    return re.sub(regex, r'\1', content)


def process_kana_template(content):
    """
    Replace mediawiki "kana" template http://arcturus.su/wiki/Template:Kana
    With our own shortcode.
    """
    regex = r"{{kana\|(.*?)}}"
    return re.sub(regex, r'{{< kana "\1" >}}', content)


def process_tiles_template(content):
    """
    Replace mediawiki "mj" tiles extension
    With our own shortcode.
    """

    # remove space at the start of string
    content = content.replace('\n {{#mjt:', "\n{{#mjt:")

    regex = r"{{#mjt:(.*?)}}"
    for x in list(re.finditer(regex, content)):
        group = x.group(0)
        match = re.findall(regex, group)[0]

        new_string = []
        for i, symbol in enumerate(match):
            """
            Because of difference between tiles hand visualizer. We need to do string transforms.

            Replace
            7'89s
            with
            -789s

            Replace
            55"5
            with
            5-5-55s
            """
            if symbol == "'":
                new_string.insert(i - 1, '-')
                continue

            if symbol == '"':
                new_string.insert(i - 1, '-')
                new_string.insert(i, new_string[i - 2])
                new_string.insert(i + 1, '-')
                continue

            new_string.append(symbol)

        content = content.replace(group, ("{{< t %s >}}" % "".join(new_string)).encode('utf-8'))

    return content


def process_template_blocks(content):
    """
    Replace mediawiki template block with escaped text.
    """

    # one line
    regex = r"{{(?!<)([\S\s]*?)}}"
    content = re.sub(regex, r'```\1```', content)
    return re.sub(regex, r'```\1```', content)


def process_infobox_blocks(content):
    """
    Replace mediawiki multiline infoboxes with escaped text.
    """
    regex = r"{{infobox ([\S\s]*?)}}\n'"
    content = re.sub(regex, r"```\1```\n\n'", content)

    regex = r"{{infobox ([\S\s]*?)}}\n\n"
    content = re.sub(regex, r'```\1```\n\n', content)

    return content


def process_wiki_links(content):
    """
    Replace [pinzu](pinzu "wikilink") with link name for now.
    """
    regex = r'\[(.*?)\]\((.*?) "wikilink"\)'
    return re.sub(regex, r'\1', content)


def process_categories(content):
    """
    Extract page categories and remove them from wiki file.
    """
    regex = r'\[\[Category:(.*?)\]\]'
    categories = re.findall(regex, content)
    content = re.sub(regex, r'', content)
    return categories, content


def process_table_headers(content):
    regex = r"\|\+ (.*?)\n"
    return re.sub(regex, r'| \1', content)


def remove_escaping(content):
    """
    Pandoc escaped shortnames and wiki tags that we created before.
    We want to revert these escaped symbols.
    """
    content = content.replace('{{\<', '{{<')
    content = content.replace('\>}}', '>}}')
    content = content.replace('\`\`\`', '```')
    return content


if __name__ == '__main__':
    main()
# coding=utf-8
import os
import re
import subprocess

from lxml import etree
from slugify import slugify


def main():
    skip_titles_start_with = [
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

    skip_pages = [
        u"2015 WAML season 1 results",
        u"List of North American riichi mahjong clubs",
        u"Mahjong Guide Quick-Fire Tournament Series",
        u"World Riichi Mahjong League",
        u"Tournament blocks",
        u"Gemma Sakamoto",
        u"Svenska Mahjongförbundet",
        u"Nihon Pro Mahjong Kyoukai",
        u"Osamuko's Japanese Mahjong Blog",
        u"Górnośląski Związek Madżonga",
        u"Summer Global Open",
        u"WRML season 4",
        u"Summer 2014 Bugmoney Tournament",
        u"Mahjong Danmark",
        u"Replay/Youtube",
        u"2018 North American Open",
        u"Himeron",
        u"Saikouisen Nihon Pro Mahjong",
        u"World Riichi Championship",
        u"Hiroshi Yamai",
        u"List of Tenhou.net events",
        u"European Riichi Mahjong Championship",
        u"List of mahjong clubs",
        u"Mahjong tournaments",
        u"List of Japanese organizations",
        u"NYC International Riichi Open",
        u"UK Riichi Mahjong Open",
        u"Seattle Riichi Mahjong Club",
        u"Swedish Open Riichi Mahjong Championship 2014",
        u"2020 World Riichi Championship",
        u"Marchao",
        u"European Ranking System",
        u"List of tournament systems",
        u"Osamuko OTP Tournament",
        u"2014 World Riichi Championship",
        u"Deutsche Mah-Jongg Liga",
        u"Northwestern University Riichi Mahjong",
        u"Chicago Area Mahjong",
        u"Real Mahjong Unit",
        u"2017 Anime Central Mahjong Tournament",
        u"ZOO",
        u"Tanoshii Tournament",
        u"2016 Anime Central Mahjong Tournament",
        u"2015 Anime Central Mahjong Tournament",
        u"North American Open",
        u"2015 WAML season 1 ungrouped players",
        u"2019 Anime Central Mahjong Tournament",
        u"2014 Anime Central Mahjong Tournament",
        u"United Kingdom Mahjong Association",
        u"List of European tournaments",
        u"2019-2020 M League Season",
        u"2017 International Online Riichi Mahjong Competition",
        u"Doman Mahjong",
        u"PML Mugboney Bug Team Tournament",
        u"Martin Rep",
        u"2019 International Online Riichi Mahjong Competition",
        u"Catfood Bowl S0 Tournament",
        u"2015 WAML season 1",
        u"Mahjong programming tests",
        u"2016 European Riichi Mahjong Championship",
        u"United States Professional Mahjong League",
        u"Pacific Mahjong League",
        u"Saikyosen",
        u"List of mahjong events - 2015",
        u"Ukrainian Mahjong Federation",
        u"Aotenjou",
        u"Anime Central Mahjong Tournament",
        u"International Online Riichi Mahjong Competition 2015",
        u"Japan Professional Mahjong League",
        u"Light Mahjong Club",
        u"Riichi Book 1",
        u"Mahjong News",
        u"Koushin Asakura",
        u"Comparative rankings for WRC",
        u"1st North American Riichi Open",
        u"2016 Osamuko Invitational",
        u"List of North American tournaments",
        u"International Reporting Guidebook",
        u"Ittsu vs sanshoku",
        u"Chankan/Replays",
        u"Terminology",
        u"List of terminology by usage category",
        u"Tenhou Meijinsen",
        u"2018 Anime Central Mahjong Tournament",
        u"Mahjong play styles",
        u"DFW Mahjong 2018 Riichi Open",
        u"Nederlandse Mahjong Bond",
        u"Touhou Unreal Mahjong",
        u"Saki Cup Japanese Mahjong Group Tournament",
        u"Targeting",
        u"Club Riichi de Montréal",
        u"Nodocchi.moe",
        u"Bugmoney Tournament",
        u"List of terminology translations",
        u"Tengokuhai",
        u"International Online Riichi Mahjong Competition",
        u"List of mahjong blogs",
        u"Mahjong Union",
        u"WRML season 1",
        u"World Amateur Mahjong League",
        u"Saki (series)",
        u"http://arcturus.su/wiki/Saki_(series)",
        u"Mahjong de campo minado",
        u"North American Riichi Mahjong Association",
        u"Polska Liga Mahjonga",
        u"Fédération Française de Mah-Jong",
        u"Swedish Open Riichi Mahjong Championship 2015",
        u"Korean Mahjong League",
        u"2018-2019 M League Season",
        u"2017 LAPOM Championship",
        u"WRML season 2",
        u"WRML season 3",
        u"2018 International Online Riichi Mahjong Competition",
        u"Mahjong Broadcast Schedules",
        u"World Riichi Championship rules",
        u"101 Kyougi Renmei",
        u"Main Page",
        u"2016 International Online Riichi Mahjong Competition",
        u"2017 World Riichi Championship",
        u"What would you discard",
        u"Probability",
        u"Situational analysis",
        u"European Mahjong Association",
        u"Kindai Mahjong",
        u"M.League",
        u"Tenhou.net custom rooms",
        u"Kyoku",
    ]

    current_directory = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(current_directory, 'arcturus/arcturussu_mjw.xml')
    export_dir = os.path.join(current_directory, 'arcturus', 'export')

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

            if page and not any([page['title'].startswith(x) for x in skip_titles_start_with]) and not page['title'] in skip_pages:
                pages[page['title']] = page

    print('pages', len(pages.keys()))

    for key, page in pages.items():
        # for debug
        if page['id'] != '51':
            continue

        title = page['title']
        print(page['title'], page['id'])

        file_name = title.replace(' ', '_').replace('/', '__')
        with open(os.path.join(export_dir, '%s.wiki' % file_name), 'w') as f:
            f.write(page['text'].encode('utf-8'))

        slug = slugify(title)
        wiki_file_path = os.path.join('%s.wiki' % slug)
        md_file_path = os.path.join('%s.md' % slug)
        final_md_file_path = os.path.join(current_directory, '..', 'hugo', 'content', 'english', 'riichi', 'wiki', os.path.join('%s.md' % slug))

        with open(wiki_file_path, 'w') as f:
            content = page['text']

            categories, content = process_categories(content)

            content = process_special_cases(content)
            content = process_infobox_blocks(content)
            content = process_kana_template(content)
            content = process_tiles_template(content)
            content = process_template_blocks(content)
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

        os.remove(wiki_file_path)
        os.rename(md_file_path, final_md_file_path)

        with open(final_md_file_path, 'r') as f:
            content = f.read()

        content = remove_escaping(content)

        with open(final_md_file_path, 'w') as f:
            content = process_wiki_links(content)

            # insert header
            f.seek(0, 0)
            f.write('+++\n')
            f.write('title = "%s"\n' % title)
            f.write('id = "%s"\n' % page['id'])
            f.write('categories = "%s"\n' % ", ".join(categories))
            f.write('+++\n\n')

            f.write(content)


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
    regex = r"{{infobox ([\S\s]*?)}}\n\n"
    return re.sub(regex, r'```\1```\n\n', content)


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


def process_special_cases(content):
    content = content.replace('|+ Sample successful attempts', '| Sample successful attempts')
    return content


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
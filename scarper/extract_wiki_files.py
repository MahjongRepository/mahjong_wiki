#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import json
import os

from lxml import etree

current_directory = os.path.dirname(os.path.abspath(__file__))
export_dir = os.path.join(current_directory, "arcturus", "export")
xml_file = os.path.join(current_directory, "arcturus", "arcturussu_mjw.xml")


def main():
    skip_titles_start_with = [
        "Category:",
        "Category talk:",
        "Help talk:",
        "Help:",
        "Template talk:",
        "Template:",
        "MediaWiki talk:",
        "MediaWiki:",
        "File talk:",
        "File:",
        "Project:",
        "User talk:",
        "User:",
        "Talk:",
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
        u"List of mahjong clubs outside Japan",
        u"Tenhou.net client",
        u"Saikyo no Mahjong 3D",
        u"Janryumon",
        u"Professional League Game Rules",
    ]
    pages = []
    with open(xml_file, "r") as f:
        root = etree.fromstring(f.read())

        for page_tag in root.findall("page", namespaces=root.nsmap):
            # skip system pages with redirects
            if page_tag.find("redirect", namespaces=root.nsmap) is not None:
                continue

            page = {}
            for child in page_tag:
                if etree.QName(child).localname == "title":
                    page["title"] = child.text

                if etree.QName(child).localname == "id":
                    page["id"] = child.text

                if etree.QName(child).localname == "revision":
                    page["text"] = child.find("text", namespaces=root.nsmap).text

            if not page:
                continue

            if page["title"] in skip_pages:
                continue

            if any([page["title"].startswith(x) for x in skip_titles_start_with]):
                continue

            pages.append(page)

    pages = sorted(pages, key=lambda x: x["title"])
    print("pages", len(pages))

    with open(os.path.join(export_dir, "_meta.json"), "r") as f:
        pages_meta_data = json.loads(f.read())

    for page in pages:
        title = page["title"]
        file_name = title.replace(" ", "_").replace("/", "__")

        with open(os.path.join(export_dir, "%s.wiki" % file_name), "w") as f:
            f.write(page["text"].encode("utf-8"))

        if not pages_meta_data.get(file_name):
            pages_meta_data[file_name] = {"mapped": {}}

        pages_meta_data[file_name]["title"] = page["title"]
        pages_meta_data[file_name]["id"] = page["id"]

    with open(os.path.join(export_dir, "_meta.json"), "w") as f:
        f.write(json.dumps(pages_meta_data, indent=2))


if __name__ == "__main__":
    main()

+++
title = "Happoubijin"
arcturus_wiki_id = "3092"
updated = "2015-03-31T08:46:34Z"
tags = ["Terminology", "Machi"]
+++

```machi
|kanji = 八方美人
|english = *unnamed*
|fu = Variable
|type = 8
|available = 22
|tilePattern =
|gameExample =
```

**Happoubijin** {{< kana "八方美人" >}} is a tile wait pattern that creates a wait on 8 consecutive
tiles. The pattern is named likely as a pun; the name can be interpreted as "a person who is
beautiful from all angles" or "everybody's friend". It also starts with {{< kana "八" >}} for eight
the number of waits.

## Pattern

```machi
|pattern = 3334567888m000z
|tilewaits = 23456789m
```

The pattern for happoubijin resembles the nine-sided chuuren poutou wait, with two triplets and all
the tiles in between. The difference is that the happoubijin wait is shorter, with 5 tiles, not 8,
separating the triplets. Additionally, unlike the chuuren wait, the triplets cannot be 1 or 9, as
that would lower the number of available waits to 7. The construction of the waiting patterns is
similar; this example hand contains:

- A 38m shanpon wait.
- A 258m ryanmenten wait.
- A 369m ryanmenten wait.
- 4m and 7m tanki waits.

## Fu

This pattern generates 2 fu for a tanki wait only if it is won with either of the tiles next to the
triplets. Otherwise, the hand is won on a shanpon or ryanmen wait, and so no fu is scored.

## External links

`Navbox machi`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Happoubijin)

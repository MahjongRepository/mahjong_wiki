+++
title = "Machi"
arcturus_wiki_id = "267"
updated = "2019-01-13T06:23:53Z"
tags = ["Terminology", "Strategy", "Machi"]
+++

**Machi** {{< kana "待ち" >}} is the Japanese term for "wait patterns". Given any mahjong hand at
any instance, players are waiting for specific tiles either to develop their hands or complete it.
Wait patterns arise during hand development, when mahjong tiles in possession in the hand are in
need of other tiles in order to complete **[mentsu]({{< ref "/riichi/terminology/mentsu.md" >}})**
(tile groups) or the entire hand. Wait patterns during
[tenpai]({{< ref "/riichi/strategy/tenpai.md" >}}) are of particular interest, as they indicate
winning tiles. Players in tenpai must know their waiting tiles, or else end up missing a winning
tile.

Five patterns here are classed as "basic wait patterns". These five patterns occur frequently; and
they are not dependent on other patterns for formation. A combination of any of these five,
including themselves, can form more complicated patterns.

## Overview

Many different patterns arise during the course of hand development. Once a hand reaches tenpai,
being able to interpret the hand's available winning tiles is a vital skill. If a player does not
correctly read their winning tiles, they may miss a valid win, or they may commit a
[chombo]({{< ref "/riichi/rules/chombo.md" >}}) with an illegal win call: either by calling a win on
a tile that does not complete the hand, or calling [ron]({{< ref "/riichi/rules/naki.md" >}}) while
[furiten]({{< ref "/riichi/strategy/furiten.md" >}}) due to a tile that they did not realize would
complete the hand.

The most commonly occurring wait patterns have been given names, to make them more easily
recognizable. More complex waits can arise involving a large number of potential configurations of
the hand. This is especially true of hands with a large number of tiles in the same suit, most
notably those aiming for [chinitsu]({{< ref "/riichi/yaku/chiniisou.md" >}}). Knowing the basic wait
patterns also helps to combine them to interpret complex hands, which may have as many as 8 weights
(not counting the special cases of [chuuren poutou]({{< ref "/riichi/yakuman/chuuren-poutou.md" >}})
and [kokushi musou]({{< ref "/riichi/terminology/waits/kokushi-musou.md" >}}), which are easily
recognizable).

### Wait counts

The waiting patterns can be analyzed using two numbers: **n-sided waits** and **n-tiles available**.
This counts the number of tile types and the number of tiles themselves.

Patterns waiting for n-sided look for the number of tile types count as winning tiles. The largest
number involves [kokushi musou]({{< ref "/riichi/terminology/waits/kokushi-musou.md" >}}) with a
13-sided wait pattern. The smallest number is 1.

As for counting the number of tiles available, this accounts every tile type having 4 copies each.
Maximum possible counts exclude tiles required in the hand. Any tiles in other players' hands, the
[dead wall]({{< ref "/riichi/rules/wanpai.md" >}}), or discarded tiles are not factored to this
count. Of course, during the course of a hand, players must take into account the number of
available tiles along with the maximum count.

## Hand development

`Main|Tile efficiency`

During hand development, it is important to understand the hand's machi for two reasons. The first
is that, when trying to bring a hand to tenpai, a player will want to maximize the number of
available tiles to bring them closer. Doing this requires interpreting the patterns of potential
groups in a similar manner to finding tile waits in a tenpai hand. The second is that furiten is
best avoided, and so a player should avoid making discards that would leave them furiten once they
reach tenpai. This can be a particular challenge when developing single-suited hands that may have a
large number of different waits.

## Basic wait patterns

These five are essentially the basic wait patterns. Upon tenpai, they only look to complete either
the last tile group or the pair.

{{< table >}}

| Name                                                          | Kanji/Kana | Header text                                         |
| ------------------------------------------------------------- | ---------- | --------------------------------------------------- |
| [Ryanmen]({{< ref "/riichi/terminology/waits/ryanmen.md" >}}) | 両面       | `machi|pattern = 000z45s00000000z|tilewaits = 36s`  |
| [Penchan]({{< ref "/riichi/terminology/waits/penchan.md" >}}) | 辺張       | `machi|pattern = 00000000000z89p|tilewaits = 7p`    |
| [Shanpon]({{< ref "/riichi/terminology/waits/shanpon.md" >}}) | 双ポン     | `machi|pattern = 000000000z44s99p|tilewaits = 4s9p` |
| [Kanchan]({{< ref "/riichi/terminology/waits/kanchan.md" >}}) | 嵌張       | `machi|pattern = 000000z35m00000z|tilewaits = 4m`   |
| [Tanki]({{< ref "/riichi/terminology/waits/tanki.md" >}})     | 単騎       | `machi|pattern = 0000000000001z|tilewaits = 1z`     |

{{</ table >}}

## Named combinations

The basic patterns can be combined for more complex patterns; and the wait patterns listed here have
taken on names.

{{< table >}}

| Name                                                                     | Kanji/Kana | Header text                                              |
| ------------------------------------------------------------------------ | ---------- | -------------------------------------------------------- |
| [Nobetan]({{< ref "/riichi/terminology/waits/nobetan.md" >}})            | ノベタン   | `machi|pattern = 000z2345p000000z|tilewaits = 25p`       |
| [Sanmenchan]({{< ref "/riichi/terminology/waits/sanmenchan.md" >}})      | 三面張     | `machi|pattern = 00000000z23456m|tilewaits = 147m`       |
| [Sanmentan]({{< ref "/riichi/terminology/waits/sanmen-nobetan.md" >}})   | 三面単     | `machi|pattern = 2345678s000000z|tilewaits = 258s`       |
| [Entotsu]({{< ref "/riichi/terminology/waits/entotsu.md" >}})            | エントツ   | `machi|pattern = 45666s11000000z|tilewaits = 36s1z`      |
| [Aryanmen]({{< ref "/riichi/terminology/waits/aryanmen.md" >}})          | 亜両面     | `machi|pattern = 6788m000000000z|tilewaits = 58m`        |
| [Ryantan]({{< ref "/riichi/terminology/waits/ryantan-and-pentan.md" >}}) |            | `machi|pattern = 4555p000000000z|tilewaits = 346p`       |
| [Pentan]({{< ref "/riichi/terminology/waits/ryantan-and-pentan.md" >}})  |            | `machi|pattern = 1222m000000000z|tilewaits = 13m`        |
| [Kantan]({{< ref "/riichi/terminology/waits/kantan.md" >}})              |            | `machi|pattern = 5777s000000000z|tilewaits = 56s`        |
| [Kantankan]({{< ref "/riichi/terminology/waits/kantan.md" >}})           |            | `machi|pattern = 3335777s000000z|tilewaits = 456s`       |
| [Tatsumaki]({{< ref "/riichi/terminology/waits/tatsumaki.md" >}})        | 竜巻       | `machi|pattern = 6667888p000000z|tilewaits = 56789p`     |
| [Happoubijin]({{< ref "/riichi/terminology/waits/happoubijin.md" >}})    | 八方美人   | `machi|pattern = 2223456777s 000z|tilewaits = 12345678s` |

{{</ table >}}

## Double yakuman patterns

These two unique patterns are linked to specific
[yakuman]({{< ref "/riichi/yakuman/yakuman.md" >}}). Under all possible tile waits with these
patterns, yakuman is ensured; under some scoring rules, winning a hand with these patterns is
awarded [double yakuman]({{< ref "/riichi/rules/variations/multiple-yakuman.md" >}}). There are no
other wait patterns with more than 8 winning tiles (although it is possible for an 8-sided wait to
include four of the same tile in such a way that a hypothetical fifth copy of the same tile would
complete the hand).

### Chuuren poutou kyuumen machi

`Main|Chuuren poutou`

```machi
|pattern = 1112345678999s
|tilewaits = 123456789s
```

### Kokushi musou 13 machi

`Main|Kokushi musou`

```machi
|pattern = 19m19p19s1234567z
|tilewaits = 19m19p19s1234567z
```

## Complex patterns

`main|Complex machi`

These combinations involve patterns that do not have specific names. Instead, they use combined
forms of the other patterns. Furthermore, they mostly consist of consecutive, or closely
consecutive, numbered tiles. Recognition of these patterns can produce some significantly powerful
waits, which may be immune to [suji]({{< ref "/riichi/strategy/suji.md" >}}) and have large numbers
of waiting tiles.

## Related terminology

### Hadaka tanki

`main|Hadaka tanki`

**Hadaka tanki** refers to when a player has made four [tile
calls]({{< ref "/riichi/rules/naki.md" >}}) (other than added kans), meaning that the hand is left
with a single concealed tile for completion. The hand is necessarily tenpai with a tanki wait. Such
a hand is very difficult to defend with, because the player will only have two tiles to choose from.
Instead, the player opts for a complete attack posture.

### Jigoku

`main|Jigoku`

**Jigoku** {{< kana "地獄" >}} refers to a [tanki]({{< ref "/riichi/terminology/waits/tanki.md" >}})
wait where two of the winning tiles are already visible to all the players. The two copies of the
winning tile are either in a discard pool or visible as [dora]({{< ref "/riichi/rules/dora.md" >}})
indicators. In English, this is commonly known as the **hell wait**, a literal translation of the
Japanese.

### Karaten

`main|Karaten`

**Karaten** {{< kana "カラテン" >}}, or **empty tenpai**, is the case where there are no tiles left
to win with, due to all potential winning tiles already having been used in the player's hand, a
discard pool, a called group, or visible as dora indicators. In some rulesets, a hand in this state
is considered noten at an [exhaustive draw]({{< ref "/riichi/rules/ryuukyoku.md" >}}).

### Nakabukure

`main|Nakabukure`

**Nakabukure** refers to when a wait is embedded in the middle of a sequence, combining with a
kanchan wait and eating up some of the available tiles. Usually this refers to a tanki wait
(**botetanki**), but it can also refer to a shanpon (**boteshanpon**).

### Takame and yasume

`main|Takame and yasume`

**Takame** is a potential winning tile which is worth more points than another, called **yasume**.

## External links

`jpwiki|聴牌`

- [ReachMahjong wait guide](http://reachmahjong.com/en/forum/viewtopic.php?f=5&t=52599)

<!-- end list -->

-

    Forum list of various patterns

<!-- end list -->

- [Tenhou wait calculator](http://tenhou.net/2/)

<!-- end list -->

-

    Wait survey quiz in [Tenhou.net]({{< ref "/riichi/" >}})

`Navbox machi` `Navbox strategy`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Machi)

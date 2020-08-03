+++
title = "Ikkitsuukan"
arcturus_wiki_id = "208"
updated = "2018-05-25T18:27:32Z"
tags = ["Yaku"]
+++

```yaku
|type = Yaku
|kanji = 一通 or 一気通貫
|english = Straight
|value = 2 han
1 han (open)
|yakuSpeed = Fast
|difficulty = Easy
|yakuCombine = \* [Pinfu]({{< ref "/riichi/yaku/pinfu.md" >}})

  - [Yakuhai]({{< ref "/riichi/rules/yakuhai.md" >}})
  - [Iipeiko]({{< ref "/riichi/yaku/iipeikou.md" >}})
  - [Chinitsu]({{< ref "/riichi/yaku/chiniisou.md" >}})

|gameExample = \* [Closed ittsuu](http://tenhou.net/0/?log=2013010402gm-0009-7447-x1ba0b4910bee&tw=3&ts=7)

  - [Ittsuu]({{< ref "/riichi/yaku/ikkitsuukan.md" >}})

```

**Ikkitsuukan** {{< kana "一気通貫" >}}, or **ittsuu** {{< kana "一通" >}} for short, is a
[yaku]({{< ref "/riichi/yaku/list-of-yaku.md" >}}), defined as three distinct [tile
groups]({{< ref "/riichi/terminology/mentsu.md" >}}) containing 123, 456, 789 of one suit.
Collectively, the three groups form a complete single suit straight of 1 through 9. Naturally, in
English terms, this hand can also be noted as a "straight", similar to the poker hand of the same
name. This hand may be played open or closed. When open, the hand loses value of one han.

## Tile diagram

{{< t 123406789m34p55s >}} Winning tile: {{< t 2p >}} or {{< t 5p >}}

### Open

{{< t 222m46s55z >}} {{< t -123s >}} {{< t -879s >}} Winning tile: {{< t 5s >}}

## Formation

While the hand shows a complete 1-9 grouping from a particular suit, it is best to view the long
cluster as three separate groups of: 123, 456, and 789. This is particularly useful to note when
needing to open the hand with such a combination. For example, having tile groups of 123, 345, 678,
and 789 does not compose this yaku, despite possessing all 1-9 in the hand.

### Counter example

{{< t 12344m56p >}} {{< t -567-789m >}} Waiting for: {{< t 4p >}} or {{< t 7p >}}

In this counter example, the tiles 1-9 for one suit are in the hand. However, ittsuu would not be
counted. In fact, this [tenpai]({{< ref "/riichi/strategy/tenpai.md" >}}) hand is lacks yaku on its
own. As it stands, it is dependent on either [chankan]({{< ref "/riichi/yaku/chankan.md" >}}),
[haitei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}), or
[houtei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}). The manzu are not grouped
as 123, 456, and 789. Instead, they are grouped as 123, 567, and 789. The 4-man function as the
[pair]({{< ref "/riichi/terminology/jantou.md" >}}) rather than belong to any of the sequences.

## Discard characteristics

Hands aiming for ittsu often lack a particular suit, as a good number of one suit is collected in
the hand.

## Compatability

`main|Yaku compatability`

`Yaku compatibility table|ITT`

Ittsuu requires three out of the four tile groups to be composed of sequences: 123, 456, and 789.
That may only leave room for one tile group of any type, such as a triplet; and so, any yaku that
requires more than one triplet, including [sanshoku
doukou]({{< ref "/riichi/yaku/sanshoku-doukou.md" >}}),
[toitoi]({{< ref "/riichi/yaku/toitoihou.md" >}}),
[sanankou]({{< ref "/riichi/yaku/sanankou.md" >}}),
[sankantsu]({{< ref "/riichi/yaku/sankantsu.md" >}}), and
[shousangen]({{< ref "/riichi/yaku/shousangen.md" >}}), is deemed incompatible.
[chiitoitsu]({{< ref "/riichi/yaku/chiitoitsu.md" >}}) is likewise incompatible as it does not use
[mentsu]({{< ref "/riichi/terminology/mentsu.md" >}}), and this disqualifies
[honroutou]({{< ref "/riichi/yaku/honroutou.md" >}}) since honroutou requires either toitoi or
chiitoi. [Tanyao]({{< ref "/riichi/yaku/tanyao.md" >}}),
[chanta]({{< ref "/riichi/yaku/chanta.md" >}}), and
[junchan]({{< ref "/riichi/yaku/junchantaiyaochuu.md" >}}) are incompatible as the 456 group
contains no terminals or honours, but the 123 and 789 groups contain terminals. Finally, Ittsuu is
incompatible with [sanshoku doujun]({{< ref "/riichi/yaku/sanshoku-doujun.md" >}}) and
[ryanpeikou]({{< ref "/riichi/yaku/ryanpeikou.md" >}}) as they each require at least three sequences
in a way that are incompatible with the sequences used for ittsuu.

### With pinfu

[Pinfu]({{< ref "/riichi/yaku/pinfu.md" >}}) requires a [wait
pattern]({{< ref "/riichi/strategy/machi.md" >}}) of either
[ryanmen]({{< ref "/riichi/terminology/waits/ryanmen.md" >}}) (open wait) or
[ryanmenten]({{< ref "/riichi/terminology/waits/sanmenchan.md" >}}) (three sided open). Any other
wait pattern disqualifies pinfu. Ryanmen waits on two tile types, while ryanmenten waits on three
tile types. Both of these wait patterns regarding ittsuu are subject to [takame and
yasume]({{< ref "/riichi/strategy/takame-and-yasume.md" >}}), where only one tile type produces a
winning hand of higher value. Winning on that one tile would produce ittsuu; while the others do
not. However, this problem is completely averted if the hand contains the full 1-9 pattern. Thus,
the waiting tiles depend on the extra tile group, which renders the problem moot.

### With honitsu and chinitsu

The development of [honitsu]({{< ref "/riichi/yaku/honiisou.md" >}}) and
[chinitsu]({{< ref "/riichi/yaku/chiniisou.md" >}}) with ittsuu is made easier, when nine tiles
(1-9) out of the thirteen of the hand is already single suited. That leaves the remaining four (plus
one winning tile) to be composed of the same suit or an honor tile. But once again, in the case of
pinfu, takame and yakume may apply here, if applicable.

With closed hands, this combination produces some very powerful hands. With honitsu, the hand
produces [mangan]({{< ref "/riichi/strategy/scoring-table.md" >}}); while it is
[baiman]({{< ref "/riichi/strategy/scoring-table.md" >}}) with chinitsu.

## External links

`jpwiki|一気通貫`

`Navbox yaku`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Ikkitsuukan)

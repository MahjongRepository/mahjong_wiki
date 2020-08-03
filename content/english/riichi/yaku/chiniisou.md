+++
title = "Chiniisou"
arcturus_wiki_id = "242"
updated = "2016-01-07T22:05:26Z"
tags = ["Yaku"]
+++

```yaku
|type = Yaku
|kanji = 清一色
|english = Flush
|value = 6 han (closed)
5 han (open)
|yakuSpeed = Slow
|difficulty = Medium
|yakuCombine = \* [Riichi]({{< ref "/riichi/rules/riichi.md" >}})

  - [Ippatsu]({{< ref "/riichi/yaku/optional/ippatsu.md" >}})
  - [Mentsumo]({{< ref "/riichi/yaku/menzenchin-tsumohou.md" >}})
  - [Pinfu]({{< ref "/riichi/yaku/pinfu.md" >}})
  - [Tanyao]({{< ref "/riichi/yaku/tanyao.md" >}})
  - [Iipeiko]({{< ref "/riichi/yaku/iipeikou.md" >}})
  - [Toi toi]({{< ref "/riichi/yaku/toitoihou.md" >}})
  - [San ankou]({{< ref "/riichi/yaku/sanankou.md" >}})
  - [Ryanpeiko]({{< ref "/riichi/yaku/ryanpeikou.md" >}})
  - [Chiitoitsu]({{< ref "/riichi/yaku/chiitoitsu.md" >}})
  - [Junchan]({{< ref "/riichi/yaku/junchantaiyaochuu.md" >}})

|gameExample = \* Menchinitsu (closed).

  - With.
  - With.

```

**Chiniisou** {{< kana "清一色" >}} is a standard yaku. This yaku is composed of tiles in one suit
only. Chinitsu is worth 6 han, but it decreases to 5 han when opened. This yaku is usually referred
to as **chinitsu** or, occasionally, **chinichi**.

## Tile patterns

**Using [pinzu]({{< ref "/riichi/rules/mahjong-equipment.md" >}}):**

```machi
|pattern = 1234455778899p
|tilewaits = 45p
```

**Using [manzu]({{< ref "/riichi/rules/mahjong-equipment.md" >}}):**

```machi
|pattern = 2345566677899m
|tilewaits = 1478m
```

**Using [souzu]({{< ref "/riichi/rules/mahjong-equipment.md" >}}):**

```machi
|pattern = 1233456667788s
|tilewaits = 36789s
```

## Formation

As defined, this yaku is formed by collecting tiles of one suit. Therefore, tiles not of a
particular suit are regularly discarded. As a consequence, a player aiming for a chinitsu may be
very easily detected via discards alone.

### Complex wait patterns

Chinitsu is notorious for developing complex wait patterns. This is due to the homogenous nature of
the yaku. The number of potential waiting tiles may range from one tile of the suit to all nine
tiles. Strings of consecutive numbers enable this complexity. Without the help of computers, this
complexity increases the difficulty in determining the winning tiles upon tenpai.

### Compatability

`main|Yaku compatability`

`Yaku compatibility table|CHN`

Chinitsu requires a single suit, so that deems this yaku incompatible with other yaku that demand
other tile types. That includes [yakuhai]({{< ref "/riichi/rules/yakuhai.md" >}}),
[shousangen]({{< ref "/riichi/yaku/shousangen.md" >}}), as well as
[sanshoku]({{< ref "/riichi/yaku/sanshoku-doujun.md" >}}) and [sanshoku
doukou]({{< ref "/riichi/yaku/sanshoku-doukou.md" >}}). Since chinitsu implies
[honitsu]({{< ref "/riichi/yaku/honiisou.md" >}}), the latter is not counted together. If combined
with [chanta]({{< ref "/riichi/yaku/chanta.md" >}}), the hand is actually
[junchan]({{< ref "/riichi/yaku/junchantaiyaochuu.md" >}}), so that yaku is counted instead.
Finally, chinitsu and [honroutou]({{< ref "/riichi/yaku/honroutou.md" >}}) would require a hand
containing at most eight tiles (the 1s and 9s of one suit), which is impossible.

### Yakuman

Due to the relatively high value of this yaku, chinitsu may be involved in the formation of [kazoe
yakuman]({{< ref "/riichi/yakuman/kazoe-yakuman.md" >}}). Especially when closed, the 6-han is
enough to be almost half necessary to acquire 13-han. Naturally, other yaku and/or dora will have to
compose the rest. Though, one particular pattern may form as the yakuman, [chuuren
poutou]({{< ref "/riichi/yakuman/chuuren-poutou.md" >}}).

## Value

As a standalone yaku, chinitsu is at least a
[mangan]({{< ref "/riichi/strategy/scoring-table.md" >}}), even when open. To regain the lost han as
an open hand, it simply takes just one dora, or a combination with another yaku, just to bring the
hand up to its closed value of a haneman.

## External links

`jpwiki|清一色`

- [Bamboo flash game](http://www.gamedesign.jp/flash/bamboo/bamboo.html)

<!-- end list -->

-

    Game designed with [sou]({{< ref "/riichi/rules/japanese-mahjong.md" >}}) tiles only to train reading chinitsu hands.

`Navbox yaku`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Chiniisou)

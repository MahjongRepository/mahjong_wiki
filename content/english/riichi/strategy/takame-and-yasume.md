+++
title = "Takame and yasume"
arcturus_wiki_id = "2441"
updated = "2015-09-06T12:40:47Z"
tags = ["Terminology", "Strategy"]
+++

**Takame** {{< kana "高目" >}} and **yasume** {{< kana "安目" >}} involve
[tenpai]({{< ref "/riichi/strategy/tenpai.md" >}}) hands, where the different multiple waiting tiles
produces different value based on yaku and/or dora. This deals with the situation, where one group
of waiting tiles may produce a hand of lower value than the other group of waiting tiles. **Takame**
refers to the tile wait(s) producing the greater hand value, while **yasume** wins with the tile(s)
of a lesser value. Often, the situation determines whether a hand produces specific
[yaku]({{< ref "/riichi/yaku/yaku.md" >}}) or not. A classic example involves
[atozuke]({{< ref "/riichi/strategy/atozuke.md" >}}), where the lesser valued tile prevents a hand
from winning while the preferred tile does.

Of course, this condition may be nullified with hands of
[mangan]({{< ref "/riichi/strategy/scoring-table.md" >}}) or greater. This is simply due to the
ranges of han required to produce mangan or greater. For example, a haneman hand is worth 6 or 7
han. So, the need to increase a hand's value from 6 han to 7 han becomes irrelevant, as the points
awarded is the exact same. Of course, the condition is invoked again when the value differs from 7
han to 8 han.

In relation of [tile waits]({{< ref "/riichi/strategy/machi.md" >}}), this condition potentially
affects any hand with multiple tile waits. Any hand implementing only a
[penchan]({{< ref "/riichi/terminology/waits/penchan.md" >}}),
[kanchan]({{< ref "/riichi/terminology/waits/kanchan.md" >}}) or
[tanki]({{< ref "/riichi/terminology/waits/tanki.md" >}}) wait usually cannot be affected, since
there is only one type of winning tile. Other wait patterns, including a combination of multiple
single waits such as [nobetan]({{< ref "/riichi/terminology/waits/nobetan.md" >}}), may lead to
yasume and takame. Certain multiple waits, such as the [kokushi
musou]({{< ref "/riichi/terminology/waits/kokushi-musou.md" >}}) 13-sided wait, and the [chuuren
poutou]({{< ref "/riichi/yakuman/chuuren-poutou.md" >}}) 9-sided wait, are inherently immune to
this, while others may depend on the precise circumstances of the hand. For instance, a ryanmen wait
that would potentially complete an [iipeikou]({{< ref "/riichi/yaku/iipeikou.md" >}}) will only have
takame and yasume if the hand is closed.

Cases involving choosing [riichi]({{< ref "/riichi/rules/riichi.md" >}}) or using
[damaten]({{< ref "/riichi/strategy/damaten.md" >}}) provide interesting scenarios. Using damaten,
players retain the ability to be selective of particular tiles to win. A player can simply decline
yasume tile(s), in order to wait for the takame tile(s). Those who call riichi may not have that
option, as using the same tactic of declining winning tiles renders the hand in
[furiten]({{< ref "/riichi/strategy/furiten.md" >}}). Such a decision may prove to be risky or
rewarding.

## Examples

- [Atozuke]({{< ref "/riichi/strategy/atozuke.md" >}})

```machi
|pattern = 11s77z
|tiles called = 9'99p444's4'35m
|tilewaits = 7z
|wait status = Takame
|yasume = 1s
```

-

    This is a special case, where only one tile can produce a valid win, while the other does not. Unless a circumstantial yaku like [haitei or houtei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}) is available, this hand has no yaku with 1s.

<!-- end list -->

- [Dora]({{< ref "/riichi/rules/dora.md" >}})-based

```machi
|pattern = 34p456m123678s11m
|tilewaits = 25p
```

-

    This is just a regular [pinfu]({{< ref "/riichi/yaku/pinfu.md" >}}) hand waiting on one of two tile types. If one of them is dora, then the hand prefers to win off of that dora tile. However, at times, it may just end up accepting the non-dora winning tile.

<!-- end list -->

- [Pinfu]({{< ref "/riichi/yaku/pinfu.md" >}}) and [tanyao]({{< ref "/riichi/yaku/tanyao.md" >}})
  potential

```machi
|pattern = 2223m678p345567s
|tilewaits = 4m
|wait status = Takame
|yasume = 13m
```

-

    In this case, the hand is waiting on three tiles. Two waits will result in pinfu (1m and 4m). Two waits will result in tanyao (3m and 4m). Winning with 4m maximizes hand value.

<!-- end list -->

- [Sanshoku]({{< ref "/riichi/yaku/sanshoku-doujun.md" >}})

```machi
|pattern = 56m456p456s22233z
|tilewaits = 4m
|wait status = Takame
|yasume = 7m
```

-

    In this case, the hand is waiting on two tiles. One tile will result in sanshoku. The other does not.

### Yakuman involved

- [Daisangen]({{< ref "/riichi/yakuman/daisangen.md" >}})

```machi
|pattern = 44m55866'6777'z
|tilewaits = 5z
|wait status = Takame
|yasume = 4m
```

-

    Tenpai hand waiting to produce either daisangen (takame) or [shousangen]({{< ref "/riichi/yaku/shousangen.md" >}}) (yasume).

<!-- end list -->

- [Chuuren poutou]({{< ref "/riichi/yakuman/chuuren-poutou.md" >}}) -
  [Example](http://tenhou.net/0/?log=2013102709gm-0009-7447-dce693b1&tw=0&ts=11)

```machi
|pattern = 1111235678999p
|tilewaits = 4p
|wait status = Takame
|yasume = 578p
```

-

    Only one tile can produce the yakuman, chuuren poutou, while the other waits produce only [chinitsu]({{< ref "/riichi/yaku/chiniisou.md" >}}).

## Other scoring conditions

Two other situations can occur where a hand scores differently depending on how it is won, not
counting yaku specifically tied to the method of winning:
[mentsumo]({{< ref "/riichi/yaku/menzenchin-tsumohou.md" >}}),
[chankan]({{< ref "/riichi/yaku/chankan.md" >}}),
[rinshan]({{< ref "/riichi/yaku/rinshan-kaihou.md" >}}), [haitei, and
houtei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}).

The first is when [akadora]({{< ref "/riichi/rules/dora.md" >}}) are in use and a hand is waiting on
a tile featuring such a tile. In this case, the hand potentially scores higher if it wins with a
dora tile than with a non-dora tile.

The second situation involves the [sanankou]({{< ref "/riichi/yaku/sanankou.md" >}}) and
[suuankou]({{< ref "/riichi/yakuman/suuankou.md" >}}) yaku. These yaku cannot be scored if the third
or fourth [koutsu]({{< ref "/riichi/terminology/mentsu.md" >}}) is completed with a
[ron]({{< ref "/riichi/rules/naki.md" >}}). As a result, the hand may score higher if won on a
[tsumo]({{< ref "/riichi/terminology/tsumo.md" >}})

These scoring aspects may additionally be combined with each other and with yasume and takame:

```machi
|pattern = 66678m22255p666s
|tilewaits = 69m5p
```

In this case, if the hand wins with a 5-pin or with 6-man, it will qualify for
[tanyao]({{< ref "/riichi/yaku/tanyao.md" >}}), but not if it wins with 9m. The winning 5-pin could
be red, giving an additional dora tile. Then there is consideration for sanankou. With a ronned
6-man or 9-man, it will qualify for sanankou. With a 6-man or a 5-pin by tsumo, it also contains
sanankou. If the winning tile is 6m or 9m, then then 666m
[ankou]({{< ref "/riichi/terminology/mentsu.md" >}}) existed in the hand already, and if a 5p is
drawn for a tsumo, then the 555p ankou can be used instead. In any case, the least desired winning
tile may be the 9-man, assuming none of the winning tiles are dora.

## External links

`Navbox machi`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Takame_and_yasume)

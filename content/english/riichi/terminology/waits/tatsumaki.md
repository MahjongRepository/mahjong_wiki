+++
title = "Tatsumaki"
arcturus_wiki_id = "3091"
updated = "2019-09-20T16:45:14Z"
tags = ["Terminology", "Machi"]
+++

```machi
|kanji = 竜巻
|english = Tornado
|fu = Variable
|type = 5
|available = 13
|tilePattern =
|gameExample = \* [Example](http://tenhou.net/0/?log=2015090315gm-00d1-0000-647ecc27&tw=0)

  - [Suuankou tanki](http://tenhou.net/0/?log=2015110914gm-0089-0000-b095eed3&tw=0&ts=1)

```

**Tatsumaki** {{< kana "竜巻" >}} is a [tile wait pattern]({{< ref "/riichi/strategy/machi.md" >}})
that uses a combination of [ryanmen]({{< ref "/riichi/terminology/waits/ryanmen.md" >}}),
[shanpon]({{< ref "/riichi/terminology/waits/shanpon.md" >}}), and
[tanki]({{< ref "/riichi/terminology/waits/tanki.md" >}}) waits to create a hand waiting on 5
consecutive tiles in the same suit. This is a particularly powerful waiting pattern as it relies on
only seven tiles in the concealed portion of the hand, so even with two called [tile
groups]({{< ref "/riichi/terminology/mentsu.md" >}}), the hand can have a 5-sided wait.

## Pattern

```machi
|pattern = 000z4445666p000z
|tilewaits = 34567p
```

To determine the waiting tiles, a player must rely on the basic wait patterns. One ryanmen wait
looks for 3-pin and 6-pin. Another ryanmen waits for 4-pin and 7-pin. Finally, a tanki wait is
aiming for a 5-pin. The shanpon wait overlaps the ryanmen waits, as it goes for the 4-pin or 6-pin.

The pattern is always composed of two sets of numbered triplets. The numbers of these triplets must
be two away from each other, such as 4 and 6 from the example. The two sets of triplets are
connected by a single numbered tile inbetween the two numbers. In this case, it is 5. If one of the
triplets happen to consist of [terminals]({{< ref "/riichi/yakuman/chinroutou.md" >}}), the pattern
is still a tatsumaki. However, the number of possible waiting tiles is reduced.

## Fu

This pattern generates 2fu for a [tanki]({{< ref "/riichi/terminology/waits/tanki.md" >}}) wait only
if it is won with the middle tile. Winning with any of the four other tiles will not give any fu, as
it will be interpreted as a ryanmen wait. If interpreted for shanpon, then fu is generated based on
the tile composition.

## External links

`jpwiki|聴牌\#2つの暗刻の間に単騎の牌がはさまっている形`

`Navbox machi`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Tatsumaki)

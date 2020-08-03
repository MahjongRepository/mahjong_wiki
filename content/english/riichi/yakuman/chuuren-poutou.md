+++
title = "Chuuren poutou"
arcturus_wiki_id = "234"
updated = "2020-01-28T22:19:15Z"
tags = ["Yakuman"]
+++

```yaku
|type = Yakuman
|kanji = 九連宝燈
純正九蓮宝燈
|english = Nine gates
Pure nine gates
|value = Yakuman (closed only)
|yakuSpeed = Very slow
|difficulty = Very hard
|yakuCombine = \* [Tenhou]({{< ref "/riichi/online/tenhou/tenhou.md" >}})

  - [Chihou]({{< ref "/riichi/yakuman/tenhou-and-chiihou.md" >}})

|gameExample = \* [Chuuren](http://tenhou.net/0/?log=2014020612gm-0029-0000-d32403e3&tw=0&ts=9)

  - [Junsei chuuren](http://tenhou.net/0/?log=2015082519gm-0009-0000-fde1c6c5&tw=2&ts=1)
  - [Junsei chuuren](http://tenhou.net/0/?log=2013091303gm-0009-7447-40db80b7&tw=3&ts=3)
  - [Missed chuuren](http://tenhou.net/0/?log=2013102709gm-0009-7447-dce693b1&tw=0&ts=11)

```

**Chuuren poutou** {{< kana "九連宝燈" >}} is a yakuman and a specific instance of
[chinitsu]({{< ref "/riichi/yaku/chiniisou.md" >}}). It contains the 13-tile pattern
1-1-1-2-3-4-5-6-7-8-9-9-9 of the same suit, plus any one more tile from the suit. A special pattern
of chuuren poutou [tenpai]({{< ref "/riichi/strategy/tenpai.md" >}}) produces one with a unique
9-sided wait. In this case, the winning hand is then called **junsei chuuren poutou**
{{< kana "純正九蓮宝燈" >}}, or pure chuuren poutou. The 13-tile pattern generates a 9-sided wait
even as a normal hand with four sets and a pair. Chuuren poutou is therefore no hand shape
exception, unlike [chiitoitsu]({{< ref "/riichi/yaku/chiitoitsu.md" >}}) and [kokushi
musou]({{< ref "/riichi/terminology/waits/kokushi-musou.md" >}}).

## Tile pattern

![Chuuren poutou winning over [daisangen]({{< ref "/riichi/yakuman/daisangen.md" >}}).](Chuuren_real.jpg "Chuuren poutou winning over daisangen.")

### Regular

```machi
|pattern = 1112345578999p
|tilewaits = 6p
|yasume = 59p
```

If this hand wins with either of the yasume tiles, the hand will score only
[chinitsu]({{< ref "/riichi/yaku/chiniisou.md" >}}) rather than the yakuman.

### Nine tile wait

```machi
|pattern = 1112345678999p
|tilewaits = 123456789p
```

![Nine-Gates-anim.gif](Nine-Gates-anim.gif "Nine-Gates-anim.gif")

## Value

Chuuren is a yakuman hand. However, while tenpai, some tile waits may actually award the hand for a
considerably less value of haneman, as a closed chinitsu. Some rules award a [double
yakuman]({{< ref "/riichi/rules/variations/multiple-yakuman.md" >}}) instead when the hand goes out
from the 9-sided wait.

## Development

`main|List of chuuren configurations` The key to this yakuman is the possession of ankou of both 1's
and 9's of one suit. Since this hand uses a single suit, it overlaps
[chinitsu]({{< ref "/riichi/yaku/chiniisou.md" >}}) during development. In fact, many tenpai
formations may result in chinitsu, rather than the yakuman. This is due to the ability of chinitsu
to form some [complicated waits]({{< ref "/riichi/strategy/machi.md" >}}). If two of either group of
tiles are not available, then any attempt at this yakuman is no longer possible. Of course, that is
in addition to the collection of a string consisting of 2-8 tiles of the same suit. Likewise, if all
four copies of any one of these numbered tiles are rendered unavailable, then the yakuman is no
longer possible.

## External links

`jpwiki|九連宝燈`

- [Mathematical study](https://scirate.com/arxiv/1707.07345)
- [Chuuren](https://www.youtube.com/watch?v=-7su2I_D0y4) (YouTube)

<!-- end list -->

-

    Kojima Takeo

`Navbox yaku` `Navbox machi`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Chuuren_poutou)

+++
title = "Tenpai"
arcturus_wiki_id = "228"
updated = "2020-07-14T15:55:41Z"
tags = ["Terminology", "Strategy"]
+++

**Tenpai** {{< kana "テンパイ" >}} is also referred to as the "ready hand". It progressed from
[1-shanten]({{< ref "/riichi/terminology/iishanten.md" >}}) to effectively 0-shanten. A hand is
tenpai or "ready" when only one more tile is needed to complete the hand. The completion may be
either done by draw and/or discard, where applicable. Tenpai does not require that the completed
hand has a [yaku]({{< ref "/riichi/yaku/yaku.md" >}}), although both a completed hand and a yaku are
necessary to win. Having achieving tenpai is worth some points when a hand ends in
[ryuukyoku]({{< ref "/riichi/rules/ryuukyoku.md" >}}).

The direct opposite of tenpai is **noten** {{< kana "ノーテン" >}}. This word is a contraction of
the English **not tenpai**. A hand in this state absolutely has no chance of winning upon the
immediate draw or discard. Instead, it relies on further tile draws and discards to attain the state
of tenpai.

Overall, the recognition of a tenpai hand is one of the most important concepts of the game. Without
this recognition, then a player lacks the ability to make the best decisions on which tiles to [best
discard]({{< ref "/riichi/strategy/tile-efficiency.md" >}}).

## Tenpai conditions

Tenpai occurs under any of the four following conditions:

1.  Three [tile groups]({{< ref "/riichi/terminology/mentsu.md" >}}) and a pair
    ([jantou]({{< ref "/riichi/terminology/jantou.md" >}})). The fourth tile group needs completion.
    A majority of [wait patterns]({{< ref "/riichi/strategy/machi.md" >}}) fall under this
    condition.
2.  Four tile groups and a single tile ([tanki]({{< ref "/riichi/terminology/waits/tanki.md" >}})).
    Completion occurs when a duplicate of the pair is drawn or discarded.
3.  [Chiitoitsu]({{< ref "/riichi/yaku/chiitoitsu.md" >}}). Six distinct tile pairs and a single
    tile (also tanki).
4.  [Kokushi musou]({{< ref "/riichi/terminology/waits/kokushi-musou.md" >}}).

<!-- end list -->

- -


      Twelve different [terminals]({{< ref "/riichi/yakuman/chinroutou.md" >}}) and [honors]({{< ref "/riichi/terminology/jihai.md" >}}), by which one is paired.
      Or, the hand has thirteen different terminals and honors, by which any of them needs to be paired.

### Wait patterns

`main|Machi`

Every hand in tenpai involves some sort of wait pattern, or **machi**. Various wait patterns are
conveniently named to allow quick recognition of waiting tiles. Likewise, players who recognize
these patterns may also be able to select among them.

### Jantou

`main|Jantou`

**Jantou** are the tile pairs to a mahjong hand. Every hand, open or closed, requires at least one
tile paired. The pair must either be in the hand, or the hand must be waiting to complete the pair
while in possession of four tile groups. The latter forms the waiting pattern of
[tanki]({{< ref "/riichi/terminology/waits/tanki.md" >}}) (pair wait). In addition, certain pairings
may generate [fu]({{< ref "/riichi/yaku/fu.md" >}}). The tanki pattern generates fu, as well as with
certain [honor tiles]({{< ref "/riichi/terminology/jihai.md" >}}).

## Example tenpai hands

1\. {{< t 123456789p33m55s >}} Waiting for: {{< t 3m >}} or {{< t 5s >}}

2\. {{< t 56777p111m11144z >}} Waiting for: {{< t 4p >}}, {{< t 7p >}} or {{< t 4z >}}

3\. {{< t 111m23456s888p33z >}} Waiting for: {{< t 1s >}}, {{< t 4s >}}, or {{< t 7s >}}

4\. {{< t 22345s888m22z >}} {{< t 66-6z >}} Waiting for: {{< t 2z >}}, or {{< t 2s >}}

5\. {{< t 999p13m >}} {{< t -456p3-33z0z55s0z >}} Waiting for: {{< t 2m >}}

6\. {{< t 1z >}} {{< t -678m11-1p77-7-345s >}} Waiting for: {{< t 1z >}}

For examples 1, 2, and 3, [riichi]({{< ref "/riichi/rules/riichi.md" >}}) may be called, and/or a
player can simply win by self draw. The first two possess [yaku]({{< ref "/riichi/yaku/yaku.md" >}})
without riichi. However, the third example does not, as it stands. It requires riichi, mentsumo, or
even the likes of [haitei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}),
[houtei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}),
[rinshan]({{< ref "/riichi/yaku/rinshan-kaihou.md" >}}), or
[chankan]({{< ref "/riichi/yaku/chankan.md" >}}) to gain yaku. Regardless, the first three are
**closed tenpai** hands.

The last three examples are all open hands. Both 4 and 5 may employ
[yakuhai]({{< ref "/riichi/rules/yakuhai.md" >}}). Example 4 definitely has a yaku, via the open
call on the green dragon. Example 5 could have a yaku, if the hand is seated west or the game is in
the [west round]({{< ref "/riichi/rules/end-game-scenarios.md" >}}). The last example uses [hadaka
tanki]({{< ref "/riichi/terminology/waits/tanki.md" >}}), by which four tile calls were used to
achieve tenpai. All that remains closed is a single tile, that needs to be matched with the exact
same tile type. However, example 6 does not have yaku as it stands. It'll require
[haitei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}),
[houtei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}),
[rinshan]({{< ref "/riichi/yaku/rinshan-kaihou.md" >}}), or
[chankan]({{< ref "/riichi/yaku/chankan.md" >}}) to gain yaku.

## Karaten

`main|Karaten`
![Example of a karaten riichi, with all waiting tiles circled in red.](Dead_Wait.png "Example of a karaten riichi, with all waiting tiles circled in red.")
**Karaten** {{< kana "カラテン" >}}, or **empty tenpai**, is a state where a
[tenpai]({{< ref "/riichi/strategy/tenpai.md" >}}) hand does not have the ability to win. This is
due to unavailability of all instances of winning tiles. The "visible tiles" may either be
discarded, used as a dora indicator, or already exist in one's hand. Furthermore, they may be held
in other player's hands or even reside within the dead wall. However, the latter case is beyond a
player's visibility.

## Keishiki tenpai

`main|Keishiki tenpai` **Keishiki tenpai** {{< kana "形式聴牌" >}}, or **shaped tenpai**, applies to
hands with no yaku. Such hands still remain relevant at ryuukyoku regarding tenpai vs noten
payments. The definition of tenpai does not necessarily apply to
[yaku]({{< ref "/riichi/yaku/yaku.md" >}}).

This is a common pitfall for many beginners. Hands are built to tenpai. However, due to lack of or
limited knowledge of the yaku, players may find themselves unable to declare a win. Often, the hand
simply lacks yaku. Otherwise, [furiten]({{< ref "/riichi/strategy/furiten.md" >}}) may also be a
reason. In this state, it is still possible to produce yaku via
[haitei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}),
[houtei]({{< ref "/riichi/yaku/haitei-raoyue-and-houtei-raoyui.md" >}}), and even possibly
[rinshan]({{< ref "/riichi/yaku/rinshan-kaihou.md" >}}). This is particularly true of open hands.
For closed hands, tsumo may count as an additional option.

## Dead hand

A [dead hand]({{< ref "/riichi/rules/agari-houki.md" >}}) involves a minor penalty, but not subject
to [chombo]({{< ref "/riichi/rules/chombo.md" >}}). Dead hands often involve minor mistakes, such as
a certain number of accidental bumps to the wall or a mistake regarding [open
calls]({{< ref "/riichi/rules/naki.md" >}}). A player with a [dead
hand]({{< ref "/riichi/rules/agari-houki.md" >}}) is never considered tenpai, even if the tiles in
the hand show a state of tenpai.

## Ryuukyoku

`main|Ryuukyoku`

At the end of the hand where all tiles have been drawn other than those in the [dead
wall]({{< ref "/riichi/rules/wanpai.md" >}}), points are rewarded to tenpai hands. Yet, even while
in tenpai, players may opt to take the **noten penalty**, instead of revealing the hand.

## Agari

`main|Naki`

**Agari** {{< kana "和がり" >}} is the general call for a winning hand. Two types of winning calls
are more commonly used, depending on the source of the tile:

- [Ron]({{< ref "/riichi/rules/naki.md" >}}) - wins on discarded tiles
- [Tsumo]({{< ref "/riichi/terminology/tsumo.md" >}}) - wins on self-drawn tiles

Proper tenpai hands have a right to make these winning calls. In doing so, players must know which
tiles and yaku are needed for a win. Likewise, the recognition of [waiting
tiles]({{< ref "/riichi/strategy/machi.md" >}}) is a necessity to call on the correct tile.
Otherwise, improper calls for winning hands result in
[chombo]({{< ref "/riichi/rules/chombo.md" >}}).

## Iishanten

`main|Shanten` **Iishanten**, or 1-shanten, is the state of the hand before attaining tenpai. While
tenpai is 1-tile away from winning the hand, iishanten is 1-tile away from attaining tenpai.

With regards to tenpai, this may be a critical juncture to the hand as, in order to attain tenpai,
the player must discard a particular tile. Ideally, that tile should be a safe tile. Likewise, it
may also be a point where the player needs to decide upon
[riichi]({{< ref "/riichi/rules/riichi.md" >}}) or utilize
[damaten]({{< ref "/riichi/strategy/damaten.md" >}}) (or hidden tenpai). Regardless, when the hand
is at iishanten, a player must be ready to anticipate these kinds of decisions, when tenpai does
occur.

## External links

`jpwiki|テンパイ`

`Navbox strategy`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Tenpai)

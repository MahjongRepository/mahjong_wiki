+++
title = "Fu"
arcturus_wiki_id = "377"
tags = ["Terminology", "Yaku", "Scoring"]
+++

![Hand with [100 fu](http://tenhou.net/0/?log=2015091304gm-00c1-0000-12e0bba1&tw=2&ts=4).](Fu_100.png "Hand with 100 fu.")
**Fu** {{< kana "符" >}} (*pronounced as foo*) is a component of scoring. It takes the hand composition into consideration in terms of tile groups, wait patterns and/or win method. In addition, every hand begins with a default start value of 20 fu. To determine the final number of *fu*, the sources of fu are added up along with the base number and then rounded up to the nearest 10. One exception falls on the yaku chiitoitsu, which is defined and set at 25 fu, regardless of other factors.

## Counting Fu

### Tile groups

For shuntsu (sequences), the fu count is 0. For koutsu (triplet) and kantsu (four-of-a-kind), the fu value depends on whether they are tanyaohai (simples) or jihai/routouhai (honor/terminals).

{{< table >}}

| English        | Romaji                      | Simples | Honor/Terminal |
| -------------- | --------------------------- | ------- | -------------- |
| Open triplet   | Minkou | 2 fu    | 4 fu           |
| Open kan       | Minkan    | 8 fu    | 16 fu          |
| Closed triplet | Ankou  | 4 fu    | 8 fu           |
| Closed kan     | Ankan     | 16 fu   | 32 fu          |

{{</ table >}}

### Waits

The different basic wait patterns count for fu as well. Combination wait patterns are not listed, such as nobetan, sanmentan, and ryanmenten. Both nobetan and sanmentan counts for tanki; and ryanmenten counts for ryanmen. Other combination patterns factor fu the same as the basic patterns listed here. However, the fu counts only one time. For example, a combination of tanki and kanchan only generates 2 fu from one pattern but not for both.

As for shanpon, the fu generated with this pattern rests on the tile groupings themselves as indicated in the above table.

{{< table >}}

| English     | Romaji                        | Fu value |
| ----------- | ----------------------------- | -------- |
| Open wait   | Ryanmen | 0 fu     |
| Closed wait | Kanchan | 2 fu     |
| Edge wait   | Penchan | 2 fu     |
| Pair wait   | Tanki     | 2 fu     |

{{</ table >}}

### Yakuhai pair

If the hand's pair is of tiles that would score yakuhai in a koutsu, then this scores 2 fu. If the pair doubles up as both the round wind and the seat wind, it may score 2 fu, or 4 fu. That is dependent on which scoring rule is used for this case.

### Winning condition

  - Winning with a closed hand by ron, the hand is awarded 10 fu. These 10 fu are called *menzen-kafu* and do not count against the player for achieving pinfu.
  - A win by tsumo with an open or closed hand is worth 2 fu.
  - An exception to the fu for tsumo is a closed hand that satisfies all other criteria for pinfu. Such a hand does not score 2 fu for tsumo and instead gains the han for pinfu.
  - Depending on the scoring rules used, a hand won with a kan replacement tile may also be ineligible for the 2 fu for tsumo, instead scoring only the han for rinshan kaihou.
  - An open hand won by ron without any fu from koutsu or the waiting pattern (i.e. 20 fu) is forced to 30 fu. This is often described as being worth 2 fu for an open pinfu.

## Maximal Score

When a hand has multiple waits, or the same wait multiple ways, the way that leads to the highest-scoring hand must be chosen. This will always be the hand with the most han. This may not necessarily be the option that produces the most fu. The most common reason for this is to score pinfu. For instance:

{{< t 23345789m567p44s >}} Agari: {{< t 4m >}}

If the hand is viewed as waiting on the ryanmen {{< t 23m >}}, then it qualifies for pinfu. If, however, the hand is viewed as waiting on the kanchan {{< t 35m >}}, then it does not. It must be scored as pinfu because that is worth more points.

Pinfu is not, however, the only example of this:

{{< t 789m66678999p789s >}} Agari: {{< t 5z >}}

In this case, there are two options for interpreting the pinzu: either as {{< t 66p >}}, {{< t 678p >}}, and {{< t 999p >}}, or as {{< t 666p >}}, {{< t 789p >}}, and {{< t 99p >}}. Although the triplet of {{< t 9p >}} is worth more fu, interpreting it as the triplet would deny sanshoku, and so the hand must be interpreted as having the triplet of {{< t 6p >}}.

## Example: 1 han 110 fu

A hand with 1 han and 110 fu is an exceptionally rare hand. Its requirements are particularly limited, because the hand must be composed of all, not just some, the conditions in the following example.

Example of a **1 han and 110 fu** hand:

South player at South round:
{{< t 456m11z22z >}} {{< t 0z11s0z >}} {{< t 0z77z0z >}} Ron: {{< t 1z >}}

  - 1 han from yakuhai {{< t 7z >}}
  - base fu: 20
  - closed hand ron: 10
  - composition of hand:
      - {{< t 1z >}} open triplet: 4
      - {{< t 1s >}} closed quad: 32
      - {{< t 7z >}} closed quad: 32
      - {{< t 2z >}} double wind pair: 4

Total 102, round up to 110

This is the greatest fu count for any hand worth 1 han, and is only attainable if double winds score 4 fu. If the hand is won by tsumo, then sanankou and mentsumo will be scored; if the triplet of east is closed, then sanankou will still be scored. Finally, the last group must be a sequence, or toitoi would be scored. In these cases, this would add han to the hand.

## Example: 2 han 110 fu

A hand with 2 han and 110 fu is also possible, as in the following for the East player in the East round:

{{< t 234s1z >}} {{< t 999-9m >}} {{< t 0330z >}} {{< t 0z11p0z >}} Tsumo: {{< t 1z >}}

  - 2 han from sankantsu
  - base fu: 20
  - tsumo: 2
  - pair wait: 2
  - composition of hand:
      - {{< t 9m >}} open quad: 16
      - {{< t 3z >}} closed quad: 32
      - {{< t 1p >}} closed quad: 32
      - {{< t 1z >}} double wind pair: 4

Total 108, round up to 110

This is the greatest fu count for any hand worth 2 han. The third quad means that sankantsu must be the only yaku, but one must still be open in order to avoid sanankou. Unlike the 1 han 110 fu example, there is a little bit of leeway: for instance, the hand could be completed on a ron without a double wind pair and still score 110 fu.

With the mangan limit applied, counting this many fu for anything 3 han or higher is no longer relevant, because any han with 70 fu or more is capped at mangan. If the aotenjou scoring system is used however, high fu counts remain relevant towards point calculation.

## Open "pinfu"

Technically, pinfu cannot be a yaku while open. However, some open hands produce 0 fu based on composition alone.

{{< t 123m45p22s >}} {{< t -234p-657s >}} Waiting on: {{< t 3p >}} or {{< t 6p >}}

This is an open "yakuless" hand. When closed, it resembles that of pinfu. Counting the fu from this hand, it produces 0 fu other than the base 20 fu for every hand. A hand like this can still gain yaku worth 1-han from either chankan, haitei, or houtei. As far as hands go, this pattern generates an exception to the rule behind counting fu; and as a special case, it is granted 2 fu in order to be rounded up to 30 fu.

## Shortcuts for Counting

To be able to announce hand scores quickly, it helps to know some shortcuts for counting fu. These shortcuts take advantage of the fact that fu is always rounded up to the next 10.

  - chiitoitsu: fixed at 25 fu
  - toitoi: almost always 40 fu (see below)
  - pinfu: ron is always 30 fu, tsumo is always 20 fu
  - Closed hand without pinfu: ron is almost always 40 fu, tsumo is almost always 30 fu
  - Open hand: almost always 30 fu

These shortcuts don't work for hands that have quads since those are worth enough fu by themselves to have a significant influence on the total. In that case, it's better to simply count the fu properly.

"Almost always" means that there are a few exceptions which may raise the fu past the shortcut value. In particular, look for these elements in the hand's composition:

  - at least one concealed set of terminal/honor tiles
  - at least two open sets of terminal/honor tiles
  - one open set of terminal/honor tiles and one concealed set of simples
  - at least two concealed sets of simples

All of the above are worth 8 fu and thus may raise the total fu count by 10 when combined with the 2 fu for tsumo or for having difficult wait.

Counting fu for toitoi is a bit trickier but only *open* toitoi hands need to be considered: if you win a closed toitoi hand by tsumo, it's a yakuman (suuankou) and if you win a closed toitoi hand by ron, it's a mangan or higher (toitoi + sanankou). Also, a toitoi hand with only terminals/honors is honroutou, also worth at least a mangan. Thus, an open toitoi hand with no quads for which counting fu actually matters will almost always score 40 fu.

## External links

```jpwiki|符```
- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Fu)
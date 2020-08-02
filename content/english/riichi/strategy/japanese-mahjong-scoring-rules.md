+++
title = "Japanese mahjong scoring rules"
arcturus_wiki_id = "272"
tags = ["Strategy"]
+++

![Scoring_Table.png](Scoring_Table.png "Scoring_Table.png") Japanese mahjong features a very complex
scoring system. Nearly every mahjong hand has a value in terms of **han** and **fu**, the two
scoring factors. The han and fu are plugged into an equation to derive the value of the hand.
Certain yaku are instead given a value of yakuman (or sometimes double yakuman), the highest scoring
hands.

Under usual rules, above 4 han, the score is capped. Fu become irrelevant and the hand is scored
based solely on the han value. Since there are not a large number of possible hand values below 5
han, a scoring table is usually used, rather than calculating the values directly.

By default, most games start players at 25,000 points, with the goal of scoring at least 30,000 to
declare victory for the points leader. Both of these values are easily varied, and tournament play
in particular often starts with 30,000 points.

Under the rarely-used aotenjou rules, there is no scoring cap, and every hand is evaluated for fu
and han, regardless of value. This can result in absurdly high hand values.

## Scoring factors

### Han

**Han** {{< kana "飜" >}} is the main portion of scoring, as each yaku is assigned a value in terms
of han. Most of the yaku are valued at either 1 or 2, but the values, not counting yakuman hands, go
as high as 6 han for a closed chinitsu. Some yaku are worth one fewer han when open, and some cannot
be scored with an open hand, but many yaku are not scored the same regardless of whether the hand is
open or closed.

A hand's han value is calculated by summing together the han values of its yaku, plus the han for
each dora tile in the hand. Dora are ordinarily worth 1 han each, but a tile that is dora multiple
times is worth correspondingly more han.

In addition to knowing the yaku, players are encouraged to know their han values. This gives them
greater awareness on potential point values of the hand. This knowledge may help aiding in various
game decisions, particularly when calling riichi or abandoning the hand.

### Fu

`main|Fu`

**Fu** {{< kana "符" >}} (_pronounced as foo_) takes the hand composition into consideration in
terms of tile melds, wait patterns and/or win method. Every hand begins with a default start value
of 20 fu. To determine the final number of fu, the sources of fu are added up along with the base
number and then rounded up to the next multiple of 10. The exception is the chiitoitsu yaku, which
is fixed to 25 fu and is not rounded. While fu may be counted for hands worth 5 han or greater, it
is not necessary. At 5 han and above, the hand value is dependent only on the han count, and the fu
count is ignored. When playing with the uncommon aotenjou rule, however, the fu count is used for
hands of any han value.

### Yakuman

`main|Yakuman`

The highest-scoring combinations are the yakuman patterns. A hand completing a yakuman is not
normally scored for han and fu, but depending on the rules, it may be possible to combine multiple
yakuman for an even larger hand.

Under aotenjou rules, where there is no scoring limit, a yakuman is scored as a 13-han yaku, and a
double yakuman as a 26-han yaku.

## Scoring procedure

### Calculating basic points

To determine the point value of a hand, the following procedure is used:

1.  If the hand is a yakuman, then hand scores 8,000 basic points.
    1.  If double yakuman are used, a double yakuman scores 16,000 points.
    2.  If multiple yakuman are used, and multiple single and/or double yakuman are completed, their
        values are added together.
2.  Otherwise, determine the hand's valid yaku. Be sure not to count invalid combinations such as
    chanta + junchan.
3.  Count the han based on the yaku.
4.  Count any number of dora to the han count.
5.  If the han count is 5 or more, then counting fu is no longer necessary. Score the hand according
    to its han value:
    1.  5 han: mangan hand worth 2,000 base points.
    2.  6-7 han: haneman hand worth 3,000 base points.
    3.  8-10 han: baiman hand worth 4,000 base points.
    4.  11-12 han: sanbaiman hand worth 6,000 base points.
6.  If the han count is 4 or less, then count fu.
    1.  If the hand is not seven pairs, round the fu up to the nearest 10.
7.  To get the base points, multiply the fu value by four, and then double it for each han (**fu ×
    2<sup>(2 + han)</sup>**).
8.  If playing with kiriage mangan, round a 1,920-point hand up to a 2,000-point mangan.
9.  In any case, if the base points value would be above 2,000 for a hand with 4 or fewer han, it is
    instead a 2,000-point mangan.

### Payment multipliers

After determining the basic points, multiply based on the status as dealer and no-dealer as well as
the win by ron or tsumo.

- When a non-dealer wins by tsumo, the player is paid 1 × basic points by the other non-dealers, and
  2 × basic points by the dealer.
- When a non-dealer wins by ron, the discarding player pays the winner 4 × basic points.
- When the dealer goes out by tsumo, the player is paid 2 × basic points from all other players.
- When the dealer goes out by ron, the discarding player pays the winner 6 × basic points.

Each value to be paid is rounded up to the nearest 100.

The numbers for a ron payment are obtained by having the ronned player pay every other players
points. Because rounding is done after this reassignment of points, it is sometimes the case that a
win by tsumo is worth a few hundred more points than a win by ron.

### Honba

`main|Honba`

In addition to the points for the hand, the winner is paid a small sum of points based on the number
of honba counters on the table. Thus, as a hand is repeated, its value goes up slowly.

## End game score

`main|Final scores`

At the end of the game, the raw points are used to calculate the end game score. These are the two
or three digit +/- numbers used to reflect a player's score. Instead of 30,000 points, a player's
score may actually be displayed as +40.0.

## External links

`jpwiki|麻雀の得点計算`

- [Online hand scoring calculator](http://jbcs.info/Mahjong/hand/calculator.html)
- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Japanese_mahjong_scoring_rules)

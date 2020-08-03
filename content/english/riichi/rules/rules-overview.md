+++
title = "Rules overview"
arcturus_wiki_id = "44"
updated = "2019-12-01T16:18:59Z"
tags = ["Game rules"]
+++

Japanese mahjong is quite complex with its many rules and special cases. This article is a brief and
quick layout to the most basic rules of the game, just to get new players started. For more detailed
documentation on the rules, see [Japanese mahjong]({{< ref "/riichi/rules/japanese-mahjong.md" >}}),
as well as other articles covering various game topics.

## Tiles and suits

`main|Mahjong equipment`

- Mahjong is played by four players
- These tiles work similar to playing cards
- All in all, there are 34 tile types
- There are 4 copies each
- In total, there are 136 tiles
- The following are the three main suits, plus a class of "honor" tiles:

{{< table >}}

|                    |                                                                                 |
| ------------------ | ------------------------------------------------------------------------------- |
| `\#mjt:123456789m` | 36 tiles in the **[man]({{< ref "/riichi/rules/japanese-mahjong.md" >}})** suit |
| `\#mjt:123456789p` | 36 tiles in the **[pin]({{< ref "/riichi/rules/japanese-mahjong.md" >}})** suit |
| `\#mjt:123456789s` | 36 tiles in the **[sou]({{< ref "/riichi/rules/japanese-mahjong.md" >}})** suit |
| `\#mjt:1234567z`   | 28 [honor tiles]({{< ref "/riichi/terminology/jihai.md" >}})                    |

{{</ table >}}

## Setup

thumb|right|350px|Mahjong tiles at the initial setup before tiles are dealt.

- After tiles are shuffled, the players build walls of face-down tiles
- Each wall is 17 tiles long, double stacked
- The four walls serve as a stockpile to draw tiles from
- Each player starts with 25000 points
- Point sticks are used to keep score, when playing with real tiles

### Starting the deal

- At the start of each hand after the walls are built, players are dealt 13 tiles each
- One player throughout the game is designated as the dealer, marked by an indicator
- The dealer is begins by rolling the dice, to determine the wall break

### Seating positions

`main|Jikaze`

- The dealer is always seated East
- Player to the right of the dealer is South
- Player across the dealer is West
- Player to left of the dealer is North
- Regular turn order: East, South, West, North
- Per the turn order, each player gets 4 tiles per turn, until each has 12 tiles
- Finish the deal process by drawing one tile each, for 13 tiles in the hand
- **Dealer always gets first draw and discard**

## Objective

- Players take turns to draw and discard tiles to build complete hands (if possible)
- Develop [ready hands]({{< ref "/riichi/strategy/tenpai.md" >}}) and hopefully complete them by
  draw or discard
- [Avoid playing into other player's hands]({{< ref "/riichi/strategy/defense.md" >}}), or else lose
  points

<!-- end list -->

- **Ron**: Players who win by tile discard scores points off the discarder
- **Tsumo**: Players who win by tile draw scores points off of the other three players

## Hands and yaku

- Winning hands of 14 tiles contain four [melds]({{< ref "/riichi/terminology/mentsu.md" >}}), plus
  a pair

:\* Melds are specific groups of 3 tiles:

:\* The pair consists of any two identical tiles

:\* Melds and pairs cannot be of mixed suits

- Two exceptions to this pattern: [kokushi
  musou]({{< ref "/riichi/terminology/waits/kokushi-musou.md" >}}) and [Chii
  toitsu]({{< ref "/riichi/yaku/chiitoitsu.md" >}})

A complete hand example:

- {{< t 234m >}} {{< t 555s >}} {{< t 345p >}} {{< t 111z >}} {{< t 77z >}}

### Yaku

`main|List of yaku`

- A winning hand must have at least one [yaku]({{< ref "/riichi/yaku/list-of-yaku.md" >}}) (see [the
  list]({{< ref "/riichi/yaku/list-of-yaku.md" >}}) for pattern examples)
- A yaku is a special condition under which the win occurs, or a distinguished pattern within the
  hand's tiles
- These patterns may be viewed like poker hands
- Hands may have a combination of different yaku
- Hand value is primarily based on your yaku patterns
- Not all yaku are pattern-based, and it is not required to have a pattern-based yaku to win (e.g.,
  you may win with riichi alone)

## Strategy

- A wide variety of strategies are employed, regarding building winning hands and avoiding other
  player's hands
- Memorization of the [yaku]({{< ref "/riichi/yaku/list-of-yaku.md" >}}) is key
- Yet, players may continue to play the game simply building hands, without or with limited
  knowledge of the yaku

## See also

- [Japanese mahjong]({{< ref "/riichi/rules/japanese-mahjong.md" >}})
- [Tenhou.net rules]({{< ref "/riichi/" >}})
- [EMA rules]({{< ref "/riichi/rules/variations/ema-riichi-competition-rules.md" >}})

## External links

### Play sites

- [Tenhou.net](http://www.tenhou.net)

<!-- end list -->

-

    Select choice for English speakers ([Tenhou.net rules]({{< ref "/riichi/" >}}))

<!-- end list -->

- [Japanese Mahjong flash](http://www.gamedesign.jp/flash/mahjong/mahjong_e.html)

<!-- end list -->

-

    Flash version of the game

### Sources and guides

- [USPML rules and English language guide](http://www.uspml.com/downloads.htm)
- [Japanese Mahjong Walkthrough by HanaYoriUta](http://www.youtube.com/watch?v=mh0brmqq4sk&list=PLDC9453A66D5D2CA7)
- [Mahjong for Dummies](http://www.japanesemahjong.com)
- [General Laws](http://osamuko.com/japanese-general-laws-of-mahjong/)
- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Rules_overview)

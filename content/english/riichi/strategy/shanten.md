+++
title = "Shanten"
arcturus_wiki_id = "269"
updated = "2019-12-17T05:49:22Z"
tags = ["Terminology", "Strategy"]
+++

**Shanten** {{< kana "向聴" >}} is the number of tiles needed for reaching tenpai. It can also be
viewed as the minimum number of tile draws or tile calls required to attain tenpai.

## Shanten counts

The lower the shanten count, the closer the hand is to tenpai. Naturally, that is advantageous as
far as tile efficiency is concerned. After all, the sooner the hand gets to tenpai, then the sooner
can the hand win. For every shanten count, the hand needs any needed tile just to reduce that count.

### Iishanten

`main|Iishanten` **Example**: 1-shanten {{< t 456p111m246s1155z >}} Needs: Any {{< t 35s15z >}} to
tenpai.

### Ryanshanten

**Example**: 2-shanten {{< t 456p111m246s1255z >}} Needs: Any {{< t 12345678s125z >}} to 1-shanten.

### Sanshanten

**Example**: 3-shanten {{< t 457p111m246s1255z >}} Needs: Any {{< t 23456789p12345678s125z >}} to
2-shanten.

## Open vs closed

`main|Naki`

Often, the decision to open the hand rests on the tiles needed and the yaku most conveniently
acquired. In addition, the shanten count may play a factor too, especially at 1-shanten where a
discarded tile could put the hand into tenpai.

## Counting shanten

Multiple methods can be applied to count shanten and to quickly estimate the shanten count. The
variable names below are obvious enough, but with the extra precision that a hand or sub-hand that
has groups removed will not include pairs with tiles removed.

### Minimum shanten

Minimum shanten can easily be checked by how many useless tiles are in hand (any single 3 away, plus
single word tiles). It is important to remember that seven pairs and kokushi musou will ignore this
basic calculation.

_minimumShanten_ = min(_uselessTiles_, 6 - _pairs_, 13 - _diffTerminals_ - max(_terminalPairs_, 1)).

This method is most effective at the start of a game, and less towards the end.

### Maximum or basic shanten

Maximum shanten can easily be estimated by naïvely removing groups from the hand, then counting
pairs, then taatsu. Assuming no pairs are present, the worst shanten count is always 6. Removing
different possible groups will lead to different results: the lowest result from the universe of
removable groups is the correct result. Taking away 345 from 1123456 is entirely possible in the
process but removing 123 and 456 is clearly more optimal. With more complex hands, it is less
obvious which tiles to remove: it is essential to test every possibility **or** skip obvious
possibilities, such as if a quad occurs, it makes sense to check the first set of three, and skip
over the rest, continuing from the 4th tile and the following two.

_maximumShanten_ = max(8 - 2 \* _groups_ - max(_pairs_ + _taatsu_,
floor(_hand.length_/3)-_groups_) - min(1, max(0, _pairs_ + _taatsu_ - (4 - _groups_))), 6).

### Accurate shanten

Accurate shanten uses the maximum formula, and then includes the conditions for seven pairs and
kokushi musou.

_accurateShanten_ = min(8 - 2 \* _groups_ - max(_pairs_ + _taatsu_,
floor(_hand.length_/3)-_groups_) - min(1, max(0, _pairs_ + _taatsu_ - (4 - _groups_))), 6 - _pairs_,
13 - _diffTerminals_ - max(_terminalPairs_, 1)).

### Accurate correction (perfect shanten)

Calculating accurate shanten will give a proper result, -1 indicating a complete hand, any strictly
positive integer indicating a distance from tenpai. However, when the result is zero, there is a
chance that there are no tiles existing that could lead to creating a winning hand. From 34 possible
tiles, trying out every tile _not present in four copies_ should lead either to a complete hand
(-1), or a hand that is "still tenpai" (0). A tenpai hand that can't win does not exist, usually
because of the need of a 5th copy of a tile. This does not take into account tiles discarded or
melded by other players. Only one's hand and one's melds count against this limit.

{{< t 3456p111m >}} {{< t -333-666p >}}

If _accurateShanten_ = 0, for all possibilities of tile: keep lowest _accurateShanten_(_hand_ +
_tile_) value (-1 or 0) and add 1 (for 0 or 1). The hand above, when any other tile is added to it,
is never complete. A proper test would never make a 5th copy of 3p or 6p.

## External links

- [Calculating Shanten and Ukeire](https://pathofhouou.blogspot.com/2019/05/calculating-shanten-and-ukeire.html)

`navbox strategy`

- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Shanten)

+++
title = "Oka and uma"
arcturus_wiki_id = "409"
tags = ["Terminology", "Game rules"]
+++

At the end of the game, the raw scores are converted into an "end game score". This is most commonly referred as the plus-minus (+/-) score. The four end game scores are always set up to sum with zero. However, due to rounding errors, it is possible for the scores to equal to 1 or -1. In this case, the leader's or that of last place end game score is adjusted to ensure a zero sum.

## Oka and uma

The **oka** {{< kana "オカ" >}} is the point difference between the start score and the target score; and then it is multiplied by the number of players. In general, this can be viewed as the "ante". Typically, the start score and target score are 25,000 pts and 30,000 pts respectively. So, in this case the oka is 5,000 x 4. At the end of the game, the oka is awarded to the winning player. Not all rulesets use an oka; in this case, even if a higher target score is required to end the game, the target score is considered to be the same as the start score when calculating the scores.

The **uma** {{< kana "ウマ" >}} is the set point spread applied to the players at the end of the game. The typical point spread uses the format of ```uma|+A|+B|-B|-A```, where A \> B. Of course, the point spread does not necessarily have to follow that pattern, by which the spread does not need to be symmetric. In general, the point spread can be set to any value as long as the four numbers add up to zero. Point modifications may be used either to ease the conditions or increase the difficulty, particularly for tournament settings.

## Procedure

The end game score is calculated as follows:

1.  Raw are taken at the end of the game, naturally ordered by the final point values.
2.  Note the start score and target score point difference, find the *oka*.
3.  Subtract the target score from the final point values.
4.  Add the *oka* to the winner.
5.  Divide by 1,000.
6.  Round to the nearest integer. If the division result produces a digit of 0.5, then the number is rounded down.
7.  Apply the *uma* spread, if any.
8.  If the sum of all four does not equal to zero, then the winner's score is adjusted to produce a zero sum.

Due to rounding, the final values may not add up to zero. Therefore, it may become necessary to alter the winner's score. Usually, the difference is only +/- 1.

End score = ((Raw points + Oka - Target)/1000) + Uma

### Shortcut

![End game results with raw scores and uma scores](PlusMinus.png "End game results with raw scores and uma scores")
In general, a fast way to determine the uma scores requires the difference between two sets of numbers. First, one must find the raw score rounded to the nearest 1000 and divided by 1000 (A). Second, one must either find or know the end score difference. If necessary, that requires using the original process to determine uma (B). Now, regardless of the raw scores, the difference between the end scores and the rounded raw scores (divided by 1000) remains constant.

For this example, the shortcut applies to the distribution of ```uma```. Using the procedure above, suppose all players unrealistically finish with 25,000 points each. The target points is 30,000 as standard.

```uma compare|
|score1 = 25000
|score2 = 25000
|score3 = 25000
|score4 = 25000
|uma1 = 20
|uma2 = 10
|uma3 = -10
|uma4 = -20
|startpts = 25000
|targetpts = 30000
```

As a shortcut, the adjustment can use the scores in the first column. Then the scores can be divided by 1000 and rounded. Finally, the values in the last column can be used to adjust for the final scores. Once again, this only works with the regular ```uma``` uma.

Just to show, the values in the image to the right are used:

```uma compare|
|score1 = 35700
|score2 = 32400
|score3 = 22200
|score4 = 9700
|uma1 = 20
|uma2 = 10
|uma3 = -10
|uma4 = -20
|startpts = 25000
|targetpts = 30000
```

As a note, the values on the right hand column did not change as the corresponding raw scores differed. So, to quickly determine the end score, it is simply the rounding of the player's score divided by 1000. Then the values in the last column is applied according to placement to produce the end score.

### With different oka and uma

Naturally, with different oka and uma settings, the numbers will work themselves out differently than the ```uma``` set up.

```uma compare|
|score1 = 35700
|score2 = 32400
|scpre3 = 22000
|score4 = 9700
|uma1 = 30
|uma2 = 15
|uma3 = -15
|uma4 = -30
|startpts = 25000
|targetpts = 30000
```

The same scores are used and applied with an uma of ```Uma|30|15|-15|-30```. This time, the values in the last column are naturally different, as the uma values are different.

## Tie-breaker

![End game results with two players with the [same raw scores](http://tenhou.net/0/?log=2014011412gm-0009-7447-f4a2bbb5&tw=1).](Tiedscores.png "End game results with two players with the same raw scores.")
In the event of tied scores at the end of a game, then the tie-breaker based on the initial wind seating (or the first hand) may applied. The player closest to the dealer position takes the higher position. Afterwards, the final score procedure takes into effect. Even with tied scores, the player in the lower position will receive a lower uma score. Alternately, any oka and uma may be split evenly between the tied players, resulting in a shared placing. The specific ruleset in use determines how this is handled.

## External links

```jpwiki|ウマ\_(麻雀)```

  - [Barticle's guide](http://www.uspml.com/downloads.htm)
- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Oka_and_uma)
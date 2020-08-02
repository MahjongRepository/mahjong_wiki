+++
title = "Furiten"
arcturus_wiki_id = "240"
tags = ["Terminology", "Game rules", "Strategy"]
+++

![[Baiman tenpai](http://tenhou.net/0/?log=2012110112gm-0009-7447-14ec5c8d&tw=0&ts=4), in furiten due to 9-sou in discard. Ron cannot be called here.](Furiten.png "Baiman tenpai, in furiten due to 9-sou in discard. Ron cannot be called here.")
**Furiten** {{< kana "振聴" >}} is a restriction applied to winning hands. The player loses the ability to declare ron because of at least one winning tile in the discards. The hand in tenpai is furiten if any of that player's winning tiles are present in one's own discard pile which includes called tiles, or another player's discard pile during a turn or after its own riichi. Furiten hands are still winnable via self-draw. A call of ron while furiten is penalized by chombo, though computer games are programmed to prevent the player from declaring such a win.

In all cases, the furiten rule requires a player to be aware of all of their tile waits. Furiten applies to all waiting tiles, even that to a thirteen sided kokushi musou. If a player is tenpai but does not realize all of their possible waits, then the lack of awareness may lead to an illegal win. This is especially true of a player who has called riichi and end up passing on a winning tile.

To enforce furiten, the discard pile is specifically arranged in front of players and tile calls are still noted as part of discard piles as turned tiles. The discard arrangements allow players to keep track of who discarded which tiles. During a hand, players should take note of their status in relation to furiten and avoid calling winning hands while in furiten. Likewise, any calls for winning hands should have the discards checked for furiten. Any game involving software already checks for furiten, alerts players, and denies winning calls.

Furiten is translated as **sacred discard** in Chinese. In consequence, English terminology had made this the equivalent. However, this translation bears no relation to the Japanese term ({{< kana "振り聴牌" >}}: thrown-away tenpai).

## Rule statement

A hand in tenpai is in furiten in any of the following scenarios:

  - At least one winning tile is in one's own discard pile.
  - The hand is declared riichi and a winning tile is not claimed.
  - If the hand is not declared riichi, another player dicards a tile, and the winning tile is not claimed, then it can be in temporary furiten until the next turn.

While in furiten, the hand is unable to call ron upon a discard. However, it is still winnable via self-draw, assuming the hand has valid yaku.

### Own discard furiten

```Discard pile
|align = right
|title = Example discard pile
|tilerow1 = 1s6527z7s
|tilerow2 = 23p3s6z4s1m
|tilerow3 = 4z
|source = 2-pin in this discard applies furiten to the example hand
```

When a player is in furiten because of their own discard, it is sometimes called **permanent furiten**. This name is slightly misleading because a player can (unless they have declared riichi) change their waits to avoid this form of furiten.

All of a player's discards can be checked at any time during play, by looking at their discard pools and the rotated tiles in other players' tile calls. This leads to the most basic strategy to avoid dealing into a player's hand: tiles they have already discarded are guaranteed safe against a ron call from that player.

During hand development, it is important to bear furiten in mind. Most of the time, if a hand gets to tenpai and is furiten at that point, it indicates that the hand was inefficiently developed. This is not always the case, as sometimes a player makes a tactically correct decision and finds themselves in furiten anyway.

The most common reason for furiten, however, is when a player is already tenpai with an open hand, and does not have a guaranteed yaku. While they may have a winning tile that provides them with a yaku, if that draw another tile which completes the hand without a yaku, then they will be forced into furiten on the next discard. This most commonly occurs with a shanpon wait, one pair of which would give yakuhai, or with a ryanmen wait on 14 or 69 on a hand that would otherwise complete tanyao.

Finally, a player considering a double riichi should carefully inspect their hand before discarding; if they had a complete hand to begin with, then being in furiten will add insult to the injury of having http://osamuko.com/delicious-riichi-button-must-click-it/ passed on a tenhou or chiihou tsumo.

**Example tenpai hand**

  -   
    ```machi

|pattern = 77m34567p678s777z
|tilewaits = 258p
```

This hand waits on three different tiles. If the player has a 2-pin in their discard pile, then the hand is in furiten and may not win by ron on any tile. Even if a 5-pin or 8-pin gets discarded by an opponent, ron may not be called.

### Temporary furiten

![Ron declined, so [temporary furiten invoked](http://tenhou.net/0/?log=2014022617gm-0089-0000-ee8c6631&tw=2&ts=11) until the next own's tile draw.](TempFuriten.png "Ron declined, so temporary furiten invoked until the next own's tile draw.")
Any player in tenpai has the option to ignore a winning tile. By declining a call for ron, the player then becomes temporarily furiten until their next discard. This is called **temporary furiten**, as it expires shortly after it occurs. Although most of the time, it will apply to a discarded tile, it can also apply to a tile used to create a shouminkan. Temporary furiten cannot apply to a tile used to create an ankan, as if a player can call ron on an ankan, then they have a single-sided kokushi musou wait (and even then, this is not permitted in all rulesets). If they decline a ron, then their hand is dead and cannot be completed.

The primary purpose of the rule is to prevent a player from targeting a later player in the turn order. Once a player sees a tile discarded, they know that they can follow with the same tile and it will be safe.

While this is often a mistake to enter temporary furiten, done by a player who does not know their waits correctly or is not paying attention, it may be done deliberately in order to achieve a higher scoring hand or to target a specific player. This becomes much more common in orasu, where a player may gain little benefit from winning a hand that does not let them pass another player. Temporary furiten can also be entered by a player who does not have a guaranteed yaku, as described above. This is much less devastating than drawing the yasume tile, however, because it is only temporary.

Uncommonly, some rulesets vary the rules by allowing a tile call made by another player to cancel temporary furiten. This variation is considered by many to be a poor one.

### Permanent furiten during riichi

![[Furiten riichi](http://tenhou.net/0/?log=2015082022gm-0089-0000-a1177c83&tw=1&ts=11) applied upon declaration and discard declining a winning hand.](Furiten_riichi.png "Furiten riichi applied upon declaration and discard declining a winning hand.")
```main|Riichi```

When a player has declared riichi, the state of temporary furiten does not expire. Per the rule of riichi, a player cannot change wait. Therefore, the hand can no longer be adjusted to escape furiten. The only one opportunity to call ron comes from the first instance of a winning discarded tile. If the call to win is declined, then the only option to win the hand comes via tsumo. This rule is a critical part of defense against riichi, as it means that any tiles discarded since the declaration is safe to the riichi called player.

A player in riichi never has to worry about yasume putting them in furiten unless they are playing with ryanhan shibari. When ryanhan shibari, a riichi without a guaranteed second yaku may be quite dangerous due to furiten.

## Strategy

### Defense

```main|Defense```

The furiten rule may be applied for defensive play, which focuses on discarding safe tiles. By discarding tiles that are also visible in an opponent's discard pile, a player can avoid a ron call by that opponent. Likewise, usage of suji and kabe may also help players deduce safe tiles, based on opponent discard. This is applied when a player does not have any matching tiles in the hand with opponent discard; or a player may rather keep certain tiles, for the sake of developing the hand without tearing it apart.

### Working with furiten

Sometimes, it may be necessary to deliberately place the hand in furiten. Often, this is the result of developing the hand and defending simultaneously. To escape the bind applied by furiten, then the hand's tile wait(s) must simply change by adjusting and changing the tiles in the hand with subsequent tile draws. Of course, a player may place greater expectation on tsumo to win rather than ron.

### Furiten tsumo

Hands in furiten can still win, as furiten imposes a limit of tsumo only. For open hands, the hand requires a valid yaku. For closed hands, mentsumo will be acceptable or added.

## External links

```jpwiki|振聴```
- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Furiten)
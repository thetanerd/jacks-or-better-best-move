# jacks-or-better-best-move
Python script that will output which cards to hold in video poker for the best RTP
# How To Use
## Put In Payouts
You need to enter the payouts for different winning hands, as the ratio between payouts can change. You put this information in the first dictionary, called "payouts".
Example:
```
payouts = {
    'royal_flush' : 125000,
    'straight_flush' : 25000,
    'four_of_a_kind' : 12500,
    'full_house' : 4000,
    'flush' : 3000,
    'straight' : 2000,
    'three_of_a_kind' : 1500,
    'two_pair' : 800,
    'jacks_or_better' : 500
}
```
All that matters here is the ratio between payouts, no the absolute values, so if you you double your bet and the payouts all also double, there is no need to chnage this dictionary.
By default, the payout ratio is the same as the Video Poker at Golden Hearts Games.
## Put in Your Hand
At the very end of the file is a line that looks like this:
```
print(get_best_pattern(['6c', 'ah', '8c', '2c', 'qd']))
```
All you need to do is replace the strings in the list with the actual cards you were dealt. each card consits of exactly two characters, the first is the value of the card and the second is the suite. Values for cards 2-9 should be written with their numerical character i.e. the character 8 should be the first character for the 8 of hearts. For cards 10 through ace, use the first letter of their name, t for 10, j for jack, q for queen, k for king, a for ace. For the suite, use the first letter of the name of the suite, h for hearts, d for diamonds, c for clubs, s for spades. Examples: the 10 of diamons would be written as td, the ace of hearts would be written as ah, the 6 of clubs would be wirtten as 6c 

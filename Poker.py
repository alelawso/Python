import random

cards = {
0: '2 of Clubs',
1: '3 of Clubs',
2: '4 of Clubs',
3: '5 of Clubs',
4: '6 of Clubs',
5: '7 of Clubs',
6: '8 of Clubs',
7: '9 of Clubs',
8: '10 of Clubs',
9: 'Jack of Clubs',
10: 'Queen of Clubs',
11: 'King of Clubs',
12: 'Ace of Clubs',
13: '2 of Diamonds',
14: '3 of Diamonds',
15: '4 of Diamonds',
16: '5 of Diamonds',
17: '6 of Diamonds',
18: '7 of Diamonds',
19: '8 of Diamonds',
20: '9 of Diamonds',
21: '10 of Diamonds',
22: 'Jack of Diamonds',
23: 'Queen of Diamonds',
24: 'King of Diamonds',
25: 'Ace of Diamonds',
26: '2 of Hearts',
27: '3 of Hearts',
28: '4 of Hearts',
29: '5 of Hearts',
30: '6 of Hearts',
31: '7 of Hearts',
32: '8 of Hearts',
33: '9 of Hearts',
34: '10 of Hearts',
35: 'Jack of Hearts',
36: 'Queen of Hearts',
37: 'King of Hearts',
38: 'Ace of Hearts',
39: '2 of Spades',
40: '3 of Spades',
41: '4 of Spades',
42: '5 of Spades',
43: '6 of Spades',
44: '7 of Spades',
45: '8 of Spades',
46: '9 of Spades',
47: '10 of Spades',
48: 'Jack of Spades',
49: 'Queen of Spades',
50: 'King of Spades',
51: 'Ace of Spades'
}

def hand():
    flop = random.choices(cards), random.choices(cards), random.choices(cards)
    my_hand = random.choices(cards), random.choices(cards)
    opponent1_hand = random.choices(cards), random.choices(cards)
    turn = random.choices(cards),
    flop_turn = flop+turn,
    river = random.choices(cards),
    flop_turn_river = flop+turn+river
    print("FLOP:", flop, "\nMY HAND:", my_hand, "\nFLOP/TURN:", flop_turn, "\nFLOP/TURN/RIVER:", flop_turn_river)
hand()

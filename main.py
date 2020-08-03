from pprint import pprint
card = {}

ranks = "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
suits = "Clubs","Hearts","Diamonds","Spades"
values = tuple(range(2,14))

cards = []
for rank in ranks:
    for suit in suits:
        cards.append({ "suit": suit, "rank": rank })


pprint(cards)

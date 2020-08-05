from pprint import pprint

ranks = "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
suits = "Clubs","Hearts","Diamonds","Spades"
values = tuple(range(2,15)) 

rank_to_value = {}
for rank, value in zip(ranks, values):
    rank_to_value[rank] = value

cards = []
for rank in ranks:
    for suit in suits:                       
        cards.append({ "suit": suit, "rank": rank, "value": rank_to_value[rank] })


pprint(cards)

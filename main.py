from pprint import pprint
import signal, sys


def exit_handler(sig, frame):
    print("\nGoodbye!")
    sys.exit(0)


signal.signal(signal.SIGINT, exit_handler)

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

"""
In a game loop:
  - Learn how to shuffle the deck (will use the random module for this)
  - Learn to split the deck between a player and the computer.
  - Draw and compare the cards for each turn. 
"""

while True:

    input("This loops till you press CTRL-C ")

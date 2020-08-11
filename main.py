from pprint import pprint
import signal, sys
import random
import time as slp

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


# pprint(cards)

"""
In a game loop:
  - Learn how to shuffle the deck (will use the random module for this)
  - Learn to split the deck between a player and the computer.
  - Draw and compare the cards for each turn. 
"""
played_cards=[]
random.shuffle(cards)
player1 = cards[26:]
player2 = cards[:26]
while True:

    input("This loops till you press CTRL-C ")
    current_card = player1.pop()
    current_card2 = player2.pop()
    played_cards.append(current_card)
    played_cards.append(current_card2)
    print("Cards drawn this round:")
    for card in played_cards:
        print(card)

    if current_card["value"] == current_card2["value"]:
        print("war")
   
    else:
        winner = max(current_card, current_card2, key=lambda card: card["value"])
    
    print(f"winner {winner}")


    
# bug empty played cards after each round
    # when someone wins accumlate cards
    

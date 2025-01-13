import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
random_card = random.choice(deck)
print("Your random card:", random_card)

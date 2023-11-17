# from random import choice
import random


# coin = random.choice(["heads", "tails"])
# print(coin)

# number = random.randint(1, 10)
# print(number)


cards = ["jack", "qeen", "king"]
random.shuffle(cards)
print(cards)  # random mảng array


for card in cards:
    print(card)

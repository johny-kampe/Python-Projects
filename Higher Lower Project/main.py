from game_data import data
from art import logo, vs
import random as rand
from replit import clear


def new_star():
    star = rand.choice(data)
    return star


def find_max(followsA, followsB):
    max = ""
    if followsA > followsB:
        max = "A"
    elif followsA < followsB:
        max = "B"
    elif followsA == followsB:
        max = -1
    return max


starA = []
starB = []

starA = new_star()

score = 0
end_game = False
while end_game != True:
  print(logo)
  if score > 0:
    print(f"You're right! Current score: {score}.")
  print(f"Compare A: {starA['name']}, {starA['description']}, from {starA['country']}")
  print(vs)
  starB = new_star()
  print(f"Compare B: {starB['name']}, {starB['description']}, from {starB['country']}")

  choice = input("Who has more followers? Type 'A' or 'B': ")

  if choice == find_max(starA['follower_count'], starB['follower_count']):
    score+=1
    starA = starB
    clear()
  else:
    end_game = True
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
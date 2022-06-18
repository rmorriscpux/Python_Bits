# Simulation of plays of the High Card/Low Card minigame in Animal Crossing, assuming maximum skill.

import random

def card_selection():
    # First card between 2 and 8, inclusive.
    first_card = random.randint(2,8)
    # Second card between 1 and 9, inclusive, excluding value of first_card. 
    second_card = random.randint(1,8)
    if first_card == second_card:
        second_card += 1
    # Assume max skill: first_card is 4 or lower, go higher. first_card is 6 or higher, go lower. 5 has equal odds, just setting it to go higher here.
    return (first_card <= 5 and second_card > first_card) or (first_card > 5 and second_card < first_card)

win_count = 0
loss_count = 0

# Change this parameter for however many trials you want to run.
max_range = 2000000

for i in range(0,max_range):
    if card_selection():
        win_count += 1
    else:
        loss_count += 1

# Output results.
print("Trials:   " + str(max_range) + "\n" +
      "Wins:     " + str(win_count) + "\n" +
      "Win Pct:  " + "{:.4}".format(win_count / max_range * 100) + "%\n" +
      "Losses:   " + str(loss_count) + "\n" +
      "Loss Pct: " + "{:.4}".format(loss_count / max_range * 100) + "%")
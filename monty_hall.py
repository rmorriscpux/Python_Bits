from random import choice

def montyHallTrial(switch: bool):
    doors = {1, 2, 3}
    prize = choice(list(doors))
    selection = choice(list(doors))
    opened = choice(list(doors.difference({prize, selection})))
    if switch:
        selection = list(doors.difference({selection, opened}))[0]
    return selection == prize

def montyHallTrialQuick(switch: bool):
    return (choice([1, 2, 3]) == choice([1, 2, 3])) ^ switch

trials = 1000000
switch_win_count = 0
no_switch_win_count = 0

for i in range(trials):
    switch_win_count += int(montyHallTrialQuick(switch=True))
    no_switch_win_count += int(montyHallTrialQuick(switch=False))

print("|  Switch  |No Switch |")
print("| " + "{:.4%}".format(switch_win_count/trials) + " | " + "{:.4%}".format(no_switch_win_count/trials) + " |")
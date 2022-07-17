from cards import Card, Shoe

def war_round(playfield, p1, p2):
    # Attrition rule, auto game end.
    if len(p1) == 0:
        p2 = p2 + playfield[1] + playfield[0]
        return

    if len(p2) == 0:
        p1 = p1 + playfield[0] + playfield[1]
        return

    for i in range(0, 4):
        playfield[0].append(p1.pop(0))
        playfield[1].append(p2.pop(0))

        if len(p1) == 0 or len(p2) == 0:
            break

    if playfield[0][len(playfield[0])-1].rank['rank'] > playfield[1][len(playfield[1])-1].rank['rank']:
        p1 = p1 + playfield[0] + playfield[1]
    elif playfield[0][len(playfield[0])-1].rank['rank'] < playfield[1][len(playfield[1])-1].rank['rank']:
        p2 = p2 + playfield[1] + playfield[0]
    else:
        war_round(playfield, p1, p2)

    return

deck_start = Shoe()
deck_start.shuffle()

player_1 = []
player_2 = []

while len(deck_start.draw_stack) > 0:
    player_1.append(deck_start.draw())
    player_2.append(deck_start.draw())

turns = 0

playfield = [[],[]]

while len(player_1) > 0 and len(player_2) > 0:
    playfield[0].append(player_1.pop(0))
    playfield[1].append(player_2.pop(0))

    if playfield[0][0].rank['rank'] > playfield[1][0].rank['rank']:
        player_1 = player_1 + playfield[0] + playfield[1]
    elif playfield[0][0].rank['rank'] < playfield[1][0].rank['rank']:
        player_2 = player_2 + playfield[1] + playfield[0]
    else:
        war_round(playfield, player_1, player_2)

    turns += 1
    
    playfield[0].clear()
    playfield[1].clear()

if len(player_2) == 0:
    print("Player 1 Won In " + str(turns) + " turns.")
else:
    print("Player 2 Won In " + str(turns) + " turns.")
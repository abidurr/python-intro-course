import random

wins = 0
for n in range(10000):
    car_door = random.randint(1,3)
    our_choice = random.randint(1,3)
    monty_door = random.randint(1,3)

    while monty_door == our_choice or monty_door == car_door:
        monty_door = random.randint(1,3)

    # having the following sentence changes the choice and doubles the chance of winning
    #our_choice = 6 - our_choice - monty_door

    if our_choice == car_door:
        wins += 1

print(wins/10000)




import random

for n in range(100):
    cash = 1024

    bet = 1

    while random.choice(["win", "lose"]) == "lose":
        cash -= bet
        bet *= 2
        if cash < 0:
            break

    print(cash)

#second


number = [1,2,3,4]
import random
for i in range(4):
    number[i] = random.randint(0, 9)

print(number)

for j in range(20):
    guess = list(input("Enter guess: "))
    guess_acc = []
    for k in range(4):
        if guess == number:
            print("Exactly right!")
            break
        elif int(guess[k]) == number[k]:
            number[k] = "-"
            guess_acc.append("X")
            print("X")
        elif int(guess[k]) in number:
            guess_acc.append("O")
            print("O")
        elif int(guess[k]) not in number:
            guess_acc.append(".")
            print(".")
    print(guess_acc)

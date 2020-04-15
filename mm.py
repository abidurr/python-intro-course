number = [1,2,3,4]
save = [1,2,3,4]
import random
for i in range(4):
    number[i] = random.randint(0, 9)
    save[i] = number[i]

print(number)

for j in range(20):
    guess = list(input("Enter guess: "))
    checks = ""
    for k in range(4):
        if int(guess[k]) == number[k]:
            number[k] = "-"
            checks = checks + "X"
        elif int(guess[k]) in number:
            checks = checks + "O"
            
            number[number.index(int(guess[k]))] = "-"
        elif int(guess[k]) not in number:
            checks = checks + "."
    for l in range (4):
        number[l] = save[l]
    if checks == "XXXX":
        print("you got it!")
        break
    print(checks)


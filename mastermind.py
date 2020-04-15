number = [1,2,3,4]
import random
for i in range(4):
    number[i] = random.randint(0, 9)

print(number)

tries = 0
while tries < 20:
    guess = input("Enter guess: ")
    if len(guess) == 4:
        tries += 1
        lst = list(guess)
        count = [0,0,0]
        for i in range(4):
            if lst[i] == number[i]:
                count[1] +=1
            elif lst[i] != number[0] or lst[i] != number[1] or lst[i] != number[2] or lst[i] != number[3]:
                count[2] += 1
            count[0] = 4 - count[1] - count[2]
            print(count)
            if count[0] == 4:
                print("YOU GOT IT")
                break
    else:
        print("Enter 4-digit numbers only!")

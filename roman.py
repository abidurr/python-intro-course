roman = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L" : 50,
    "X" : 10,
    "V" : 5,
    "I" : 1
    }

def add_numerals(num1, num2):
    global roman
    no1 = list(num1)
    no2 = list(num2)

    for i in range(len(no1)):
        no1[i] = roman[no1[i]]

    for j in range(len(no2)):
        no2[j] = roman[no2[j]]


    total1 = 0
    total2 = 0

    for i in range(len(no1)):
        total1 += no1[i]

    for i in range(len(no2)):
        total2 += no2[i]

    total = total1 + total2
    romanno = list()

    while total >= 1000:
        total = total - 1000
        romanno.append("M")
    while total >= 500:
        total = total - 500
        romanno.append("D")
    while total >= 100:
        total = total - 100
        romanno.append("C")
    while total >= 50:
        total = total - 50
        romanno.append("L")
    while total >= 10:
        total = total - 10
        romanno.append("X")
    while total >= 5:
        total = total - 5
        romanno.append("V")
    while total >= 1:
        total = total - 1
        romanno.append("I")

    result = ""
    for i in range(len(romanno)):
        result = str(result) + str(romanno[i])
    


    
    return result

import random

streaksNumber = 6

numberOfStreaks = 0
randNums = []
streak = 0
for experimentNumber in range(10000):
    for i in range(100):
        randNums.append(random.randint(0, 1))

    for i in range(len(randNums)):
        if i == 0:
            pass
        elif randNums[i] == randNums[i - 1]:
            streak += 1
        else:
            streak = 0

        if streak == streaksNumber:
            numberOfStreaks += 1
    randNums = []

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))

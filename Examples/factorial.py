# factorial

def findFactorial(num):
    if num == 0:
        return 1
    else:
        return num * findFactorial(num-1)


for i in range(0, 15):
    print('%s - %s' % (i, findFactorial(i)))


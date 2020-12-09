import sys


def collatz(num):
    if num % 2:
        res = 3 * num + 1
    else:
        res = num // 2
    print(res)
    return res


while True:
    print('Type a number')
    try:
        number = int(input())
        break
    except ValueError:
        continue

while True:
    number = collatz(number)
    if number == 1:
        sys.exit()

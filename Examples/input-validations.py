import pyinputplus as pyip


def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers)


# inputValue = pyinputplus.inputEmail("Enter your email: ", timeout=5, default='213333333333')

response = pyip.inputCustom(addsUpToTen)

print(response)

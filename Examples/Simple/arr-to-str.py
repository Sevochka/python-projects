spam = ['apples', 'bananas', 'tofu', 'cats']


def makeStr(arr):
    string = ''
    if not arr:
        return 'Массив пустой'
    for i, el in enumerate(arr):
        if i == len(arr)-1:
            string += 'and '+el
            return string
        string += el + ', '


print(makeStr(spam))
print(makeStr([]))

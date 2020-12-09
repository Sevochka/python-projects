"""
    Программа, принимающая на вход tableData и выводящая все в виде равной таблицы в консоли

    apples  oranges  cherries  banana
     Alice      Bob     Carol   David
      dogs     cats     moose   goose
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


# Определяет максимальные длину каждого слова в массивах
def determineMaxLen(array):
    maxLen = []
    for col in array:
        for i in range(len(col)):
            wordLen = len(col[i])
            try:
                if maxLen[i] < wordLen:
                    maxLen[i] = wordLen
            except IndexError:
                maxLen.insert(i, wordLen)
    return maxLen


def printTable(table, maxLen):
    for col in table:
        for i, el in enumerate(col):
            spaces = maxLen[i] - len(el)
            print((" " * spaces) + el, end='  ')
        print()


printTable(tableData, determineMaxLen(tableData))

import pyinputplus as pyip

foodTypes = {
    'breadType': ['wheat', 'white', 'sourdough'],
    'proteinType': ['chicken', 'turkey', 'ham', 'tofu'],
    'chessType': ['cheddar', 'Swiss', 'mozzarella']
}


def inputMenu(food):
    for key in foodTypes:
        if food in foodTypes[key]:
            return food
    raise Exception("It's not a food")


response = pyip.inputCustom(inputMenu, 'Please, enter food')

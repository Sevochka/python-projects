# Вывод предметов из инвентаря в консоль
def displayInventory(inv):
    print("Player has:")
    summary = 0
    for i, v in inv.items():
        summary += v
        print("  " + str(v) + " " + i)
    print('Summary - ' + str(summary) + ' items')


# Добавление вещей в инвентарь
def addToInventory(inv, loot):
    for el in loot:

        if inv.get(el):
            inv[el] += 1
        else:
            inv.setdefault(el, 1)
    return inv


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inventory)
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)

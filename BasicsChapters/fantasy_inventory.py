def displayInventory(inv):
    print("Inventory:")
    total = 0
    for k, v in inv.items():
        print("%i %s" %(v, k))
        total += v
    print("Total number of items: %i" %total)


def addToInventory(inv, lootlist):
    for i in dragonLoot:
        if i not in inv.keys():
            inv[i] = 1
        else:
            inv[i] += 1


myInventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(myInventory)
print()
addToInventory(myInventory,dragonLoot)
print()
displayInventory(myInventory)
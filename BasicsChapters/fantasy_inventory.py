def displayInventory(inv):
    print("Inventory:")
    total = 0
    for k, v in inv.items():
        print("%i %s" %(v, k))
        total += v
    print("Total number of items: %i" %total)


def addToInventory(inv, lootlist):



myInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(myInventory)
addToInventory(myInventory,dragonLoot)
displayInventory(myInventory)
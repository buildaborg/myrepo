# inventory.py
'''
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        #print((inventory[v]) , ' ' , (inventory[k]))
        #print(inventory[k], end = ' ')
        print(v, k)
        item_total = item_total + 1
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
'''
def addToInventory(inventory, addedItems):
    
    for x, y in inventory.items():
        print(inventory.get(x, 0))# your code goes here

                  

inv = {'gold coin': 42, 'rope': 1}
invc = inv.copy()
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#inv = addToInventory(inv, dragonLoot)
#displayInventory(inv)

#adding new values to dictionary
for x in dragonLoot:
    invc.setdefault(x, 0)

for h in invc.keys():
    for b in dragonLoot:
        count = 0
        if b == h:
            count = count + 1
        invc[b] = invc[b] + count
            
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        #print((inventory[v]) , ' ' , (inventory[k]))
        #print(inventory[k], end = ' ')
        print(v, k)
        item_total = item_total + 1
    print("Total number of items: " + str(item_total))
displayInventory(invc)
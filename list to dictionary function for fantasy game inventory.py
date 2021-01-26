#List to Dictionary Function for Fantasy Game Inventory

#this function displays custom inventory
def displayInventory(inventory):
	print('Inventory:')
	
	items_total = 0
	#it loops over our inventory to print individual item and total items in inventory
	#	k is key, v is value
	for k,v in inventory.items():
		print(str(v) + ' ' + k)
		items_total += v

	 print('Total number of items:' + str(items_total))

#this function helps to add new item to our inventory which is given as a list 'dragonLoot'
def addToInventory(inventory, addedItems):
	for i in range(len(addedItems)):
		#if we do not have the item already in 'inv' dictionary then we initiate it
		if not(inventory.get(addedItems[i], 0)):
			inventory.setdefault(addedItems[i], 1)
		#but what if we already have the item in our dictionary then we add +1 to the value in our dictionary
		else:
			inventory[addedItems[i]] += 1

#this is the dictionary that contains all the items and their quantity
inv = {'gold coin': 42, 'rope': 1}
#this is the list using which we will fill up our dictionary
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#function calls
addToInventory(inv, dragonLoot)
displayInventory(inv)

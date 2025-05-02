
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}


def displayInventory(inventory):
    # your code goes here
    print("Inventory:")
    count = 0
    for key,value in stuff.items():  
        print(stuff[key], key)
        count = count + value
            
            

    print("total number of items:", count)

if __name__ == "__main__":
    displayInventory(stuff)

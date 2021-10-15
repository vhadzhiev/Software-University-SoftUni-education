def stock_availability(inventory, action, *args):
    if action == 'delivery':
        inventory += [*args]
    else:
        if not args:
            inventory.pop(0)
        elif type(args[0]) == int:
            inventory = inventory[args[0]:]
        else:
            inventory = [x for x in inventory if x not in [*args]]

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

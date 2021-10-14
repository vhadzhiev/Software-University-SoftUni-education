def stock_availability(*args):
    arguments = [*args]
    inventory = arguments[0]
    action = arguments[1]
    if action == 'delivery':
        for x in arguments[2:]:
            inventory.append(x)
    else:
        if len(arguments) == 2:
            inventory.pop(0)
        elif type(arguments[2]) == int:
            for i in range(arguments[2]):
                if inventory:
                    inventory.pop(0)
        else:
            for x in arguments[2:]:
                if x in inventory:
                    while x in inventory:
                        inventory.remove(x)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

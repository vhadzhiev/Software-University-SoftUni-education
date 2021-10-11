def math_operations(*args, **kwargs):
    dictionary = {**kwargs}
    list_ll = [*args]
    count = 0
    for x in list_ll:
        count += 1
        if count == 1:
            dictionary['a'] += x
        elif count == 2:
            dictionary['s'] -= x
        elif count == 3:
            if x != 0:
                dictionary['d'] /= x
        elif count == 4:
            dictionary['m'] *= x
            count = 0
    return dictionary

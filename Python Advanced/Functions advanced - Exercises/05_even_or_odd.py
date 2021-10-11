def even_odd(*args):
    result = []
    if args[-1] == 'even':
        result = [x for x in args[:-1] if x % 2 == 0]
    if args[-1] == 'odd':
        result = [x for x in args[:-1] if x % 2 != 0]
    return result

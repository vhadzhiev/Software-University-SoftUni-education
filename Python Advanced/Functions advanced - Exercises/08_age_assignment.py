def age_assignment(*args, **kwargs):
    dictionary = {}
    for x in args:
        dictionary[x] = kwargs[x[0]]
    return dictionary

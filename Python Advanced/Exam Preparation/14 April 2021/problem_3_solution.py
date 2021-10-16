def flights(*args):
    flights_dict = {}
    arguments = [*args]
    for i in range(0, len(arguments), 2):
        if arguments[i] == 'Finish':
            return flights_dict
        else:
            if arguments[i] not in flights_dict:
                flights_dict[arguments[i]] = 0
            flights_dict[arguments[i]] += arguments[i + 1]


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
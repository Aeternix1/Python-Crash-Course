#Add extra numbers to everyones favourite numbers


numbers = {
    'Ajay':[13, 29],
    'Steve':[22],
    'Timothy': [24, 29, 28],
    'Suzie': [26, 33],
    'Andrew': [32, 38],
}

for name, favourites in numbers.items():
    if len(favourites) == 1:
        print(name + "'s favourite number is:")
        for number in favourites:
            print(number)
    else:
        print(name + "'s favourite numbers are:")
        for number in favourites:
            print(number)


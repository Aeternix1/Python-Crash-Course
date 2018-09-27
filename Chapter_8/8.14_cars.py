#Function that stores information about a car in a dictionary 
#Function should always recieve a manufacturer and a model name
#Accept an arbitrary number of keyword arguments 


def make_car(make, model, **features):
    car = {} 
    car['make'] = make
    car['model'] = model
    for key, value in features.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car) 





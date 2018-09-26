#describe_city(city, country)
#Parameter for country should have a default value

def describe_city(city, country="Australia"):
    print(city.title() + " is in " + country.title())

describe_city("syndey")
describe_city("melbourne")
describe_city("hong kong")


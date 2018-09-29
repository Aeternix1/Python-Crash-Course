#Function accepts two parameters a city name and a country name
#Returns them to the following (City, Country)

def city_and_country(city, country, population=''):
    if (population):
        string = city.title() + ', ' + country.title() + ' - ' + population
    else:
        string = city.title() + ', ' + country.title()
    return string

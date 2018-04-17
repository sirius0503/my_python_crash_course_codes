def describe_city(city , country = 'UK'):
    """Prints a simple sentence from the above info"""
    print("\n" + city.title() + " is a beautiful city in country: " + 
        country.title() + "."
        )

describe_city('glasgow')
describe_city('Sheffield', country = 'UK')
describe_city(country = 'Hungary' , city = 'Budapest')

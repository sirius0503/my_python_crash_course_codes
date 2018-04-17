def city_country(city , country ):
    """Format is given"""
    return_string = '"' + city.title() + ", " + country.title() + '"'
    return return_string


saved = city_country('Newcastle','England')
print("\n" +saved)


saved = city_country('Prague','Czech Republic')
print("\n" + saved)


saved =city_country('Lisbon','Portugal')
print("\n" + saved)

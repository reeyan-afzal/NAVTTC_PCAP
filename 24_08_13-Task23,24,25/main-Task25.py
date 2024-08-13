# Converting Fuel Consumption

"""
1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
"""


def liters_100km_to_miles_gallon(liters):
    _100km_to_miles = 100 / 1.609344
    _liters_to_gallons = liters / 3.785411784
    return _100km_to_miles / _liters_to_gallons


def miles_gallon_to_liters_100km(miles):
    _distance_in_km = miles * 1.609344
    _liters_per_km = 3.785411784 / _distance_in_km
    return _liters_per_km * 100


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

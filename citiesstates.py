#mapping provinces to abbreviations
provinces = {
    'Ontario': 'ON',
    'Quebec': 'QC',
    'Manitoba': 'MB',
    'British Columbia': 'BC',
    'Alberta': 'AB'
    }

cities = {
    'ON': 'Toronto',
    'QC': 'Montreal',
    'MB': 'Winnipeg'}

cities['BC'] = 'Victoria'
cities['AB'] = 'Calgary'

print('-' * 10)
print(cities)

print('-' * 10)
print("ON province has:", cities['ON'])
print("BC Province has:", cities['BC'])

print('-' * 10)
print("Ontario's Abbreviation is:", provinces['Ontario'])
print("Quebec's Abbreviation is:", provinces['Quebec'])

print('-' * 10)
print("Ontario has:", cities[provinces['Ontario']])
print("Quebec has:", cities[provinces['Quebec']])

print('-' * 10)
print(list(provinces.items()))
print('-' * 10)
for whatever, abbrev in list(provinces.items()):
    print(whatever)
    print('#' * 10)
    print(f"{whatever} is abbreviated {abbrev}")
      
print('%' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
          
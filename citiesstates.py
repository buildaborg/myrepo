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
    'QB': 'Montreal',
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
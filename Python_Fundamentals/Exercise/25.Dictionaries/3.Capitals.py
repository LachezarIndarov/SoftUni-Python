"""
Input1
Bulgaria, Romania, Germany, England
Sofia, Bucharest, Berlin, London

Output1
Bulgaria -> Sofia
Romania -> Bucharest
Germany -> Berlin
England -> London

Input2
Bulgaria, Germany, France
Varna, Frankfurt, Paris

Output2
Bulgaria -> Varna
Germany -> Frankfurt
France -> Paris

"""

def capitals():

    country_names = input().split(", ")
    capital_cities = input().split(", ")
    result = dict(zip(country_names, capital_cities))

    for country, capital in result.items():
        print(f"{country} -> {capital}")

capitals()


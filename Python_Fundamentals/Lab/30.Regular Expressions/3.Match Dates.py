"""
https://regex101.com/
                                    Input
13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016

            Output
Day: 13, Month: Jul, Year: 1928
Day: 10, Month: Nov, Year: 1934
Day: 25, Month: Dec, Year: 1937

"""

import re

text = input()


expression = r"(?P<day>\d{2})(?P<separator>[.\/-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
matches = re.finditer(expression, text)


for match in matches:
   day = match.group("day")
   month = match.group("month")
   year = match.group("year")

   print(f"Day: {day}, Month: {month}, Year: {year}")
"""
text.txt

-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.

output:

fault@ his wasn't it but him@ judge to quick was @I
safer@ is It here@ hide @Quick@


"""
target_symbols = ["-", ",",".","!","?"]

with open('./text.txt', 'r') as file:
   for index, line in enumerate(file):
       if index % 2 == 0:
           result = ' '.join(line.strip().split()[::-1])
           for symbol in target_symbols:
               result = result.replace(symbol, '@')
           print(result)
"""
text.txt

-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.

output:

Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
Line 2: -Is this some kind of joke?! Is it? (24)(4)
Line 3: -Quick, hide here. It is safer. (22)(4)



"""
from string import punctuation

def count_symbols(line):
    punctuations_symbols = set(list(punctuation))
    letters_count = 0
    punctuations_count = 0
    for symbol in line:
        if symbol.isalpha():
            letters_count += 1
        elif symbol in punctuations_symbols:
            punctuations_count += 1
    return letters_count, punctuations_count


with open('./text.txt', 'r') as input_file, open('./output.txt', 'w') as output_file:
    for index, line in enumerate(input_file):
        letters, punctuations = count_symbols(line)
        output_file.write(f'Line{index + 1}: {line.strip()} ({letters})({punctuations})\n')



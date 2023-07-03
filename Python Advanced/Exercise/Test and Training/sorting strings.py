values = ['Pesho', 'Doncho', 'Gosho']

print(
    [-ord(x) for x in 'Doncho']   #  [-68, -111, -110, -99, -104, -111]
)

print(
    sorted(
        values,
        key=lambda x: [ord(c) for c in x]  #   ['Doncho', 'Gosho', 'Pesho']
    )
)

print(
    sorted(
        values,
        key=lambda x: [-ord(c) for c in x]  #   ['Pesho', 'Gosho', 'Doncho']
    )
)
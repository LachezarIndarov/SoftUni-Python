"""
input1
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

output1
Camembert
500
430
105
100
100
Parmesan
135
120
102
Mozzarella
125
50

input2
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

output2
Brie
150
125
Feta
515
150
Parmigiano
215
165

"""
import os


def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(
        kwargs.items(),
        key=lambda x: (-len(x[1]), x[0]),
    )

    result = []

    for name, pieces_counts in sorted_cheeses:
        result.append(name)
        result.extend(
            sorted(pieces_counts, reverse=True)
        )

        # '\n' don't use this!
        # '\n\r' for Windows
        # os.linesep
    return '\n'.join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)



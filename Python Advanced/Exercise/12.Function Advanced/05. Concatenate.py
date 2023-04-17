"""
Test Code1
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

output1
SoftUniIsGreat!

Test Code2
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

output2
I Love Python

"""
def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key, value in kwargs.items():
        text = text.replace(key,value)

    return text



print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

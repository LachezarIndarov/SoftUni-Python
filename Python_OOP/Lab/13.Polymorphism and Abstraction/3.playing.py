"""
input1
class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))

output1
Playing the guitar

input2
class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))

output2
Children are playing

"""
def start_playing(obj):
    return obj.play()

class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))

class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))
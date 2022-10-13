"""
input1
Peter
John
Katy
End

output1
Going: Peter, John, Katy
Total: 3

input2
Sam
Eddy
Edd
Kris
End

output2
Going: Sam, Eddy, Edd, Kris
Total: 4

"""

class Party:

    def __init__(self):
        self.people = []

party = Party()

while True:
    command = input()

    if command =='End':
        break
    party.people.append(command)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

"""
Input1
Adam-0888080808
2
Mery
Adam

Output1
Contact Mery does not exist.
Adam -> 0888080808

Input2
Adam-+359888001122
Ralf-666
George-5559393
Silvester-02/987665544
4
Silvester
silvester
Rolf
Ralf

Output2
Silvester -> 02/987665544
Contact silvester does not exist.
Contact Rolf does not exist.
Ralf -> 666

"""

def phone_book_information(number_of_lines, phone_book):
    for i in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")

    return True



def phone_book_info():
    phone_book = {}
    conditions = False


    while True:
        contact_information = input().split('-')

        if contact_information[0].isdigit():
            conditions = phone_book_information(int(contact_information[0]), phone_book)
        else:
            phone_book[contact_information[0]] = contact_information[1]

        if conditions:
            break


phone_book_info()







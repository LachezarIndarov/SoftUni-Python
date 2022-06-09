"""
input1
Troy
Stronger
Life Style
Troy

output1
You checked 2 books and found it.

input2
The Spot
Hunger Games
Harry Potter
Torronto
Spotify
No More Books

output2
The book you search is not here!
You checked 4 books.

input3
Bourne
True Story
Forever
More Space
The Girl
Spaceship
Strongest
Profit
Tripple
Stella
The Matrix
Bourne

output3
You checked 10 books and found it.

"""
#GitHub  - 100% Judge

book_name = input()
book_count = 0
is_book_found = False

current_book = input()
while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        print(f"You checked {book_count} books and found it.")
        break

    book_count += 1
    current_book = input()

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
"""
input1
Taxi
10
standard
kid
student
student
standard
standard
End
Scary Movie
6
student
student
student
student
student
student
Finish


output1
Taxi - 60.00% full.
Scary Movie - 100.00% full.
Total tickets: 12
66.67% student tickets.
25.00% standard tickets.
8.33% kids tickets.

input2
The Matrix
20
student
standard
kid
kid
student
student
standard
student
End
The Green Mile
17
student
standard
standard
student
standard
student
End
Amadeus
3
standard
standard
standard
Finish

output2
The Matrix - 40.00% full.
The Green Mile - 35.29% full.
Amadeus - 100.00% full.
Total tickets: 17
41.18% student tickets.
47.06% standard tickets.
11.76% kids tickets.

"""

movie_name = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0


while movie_name != 'Finish':
    free_seats = int(input())
    seats_taken = 0


    ticket_type = input()
    while ticket_type !='End':
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1


        seats_taken +=1
        if free_seats - seats_taken == 0:
            break
        ticket_type = input()
    print(f"{movie_name} - {seats_taken / free_seats * 100:.2f}% full.")
    movie_name = input()


all_tickets = standard_tickets + student_tickets + kid_tickets
print(f"Total tickets: {all_tickets}")
print(f"{student_tickets / all_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / all_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / all_tickets * 100:.2f}% kids tickets.")
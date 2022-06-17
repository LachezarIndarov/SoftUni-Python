"""
input1
1.23

output1
4

input2
2

output2
1

input3
0.56

output3
3


input4
2.73

output4
5


"""
width_of_the_cake = int(input())
length_of_the_cake = int(input())
number_of_pieces = 0



number_of_pieces = width_of_the_cake * length_of_the_cake

while True:
        eaten_pieces = input()
        if eaten_pieces == "STOP":
            print(f"{number_of_pieces} pieces are left.")
            break




        number_of_pieces -= int(eaten_pieces)

        if number_of_pieces < 0:
            print(f"No more cake left! You need {abs(number_of_pieces)} pieces more.")
            break


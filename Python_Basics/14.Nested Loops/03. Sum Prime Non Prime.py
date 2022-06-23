"""
input1
3
9
0
7
19
4
stop

output2
Sum of all prime numbers is: 29
Sum of all non prime numbers is: 13

input2
30
83
33
-1
20
stop

output2
Number is negative.
Sum of all prime numbers is: 83
Sum of all non prime numbers is: 83


"""
command = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0

while command != 'stop':
    is_prime = True
    current_number = int(command)

    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue


    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers_sum += current_number

    else:
        non_prime_numbers_sum += current_number

    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")






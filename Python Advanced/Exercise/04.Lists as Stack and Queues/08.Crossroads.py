"""
input1
10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END

output1
Everyone is safe.
3 total cars passed the crossroads.

input2
9
3
Mercedes
Hummer
green
Hummer
Mercedes
green
END


output2
A crash happened!
Hummer was hit at e.

Comments:
During the first green light (10 seconds), the Mercedes (8) passes safely.
During the second green light, the Mercedes (8) passes safely, and there are 2 seconds left.
The BMW enters the crossroads, and when the green light ends, it still has 1 part inside ('W') but has 5 seconds to leave and passes successfully.
The Skoda never entered the crossroads, so 3 cars passed successfully.

Mercedes (8) passes successfully, and Hummer (6) enters the crossroads, but only the 'H' passes during the green light.
There are 3 seconds of a free window, so "umm" passes, and the Hummer gets hit at 'e', and the program ends with a crash.

"""

from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
passed_counter = 0
crashed = False

while not crashed:
    line = input()
    if line == 'END':
        break

    if line == 'green':
        current_green = green_light
        while cars and current_green > 0:
            car = cars.popleft()
            if current_green + free_window >= len(car):
                passed_counter += 1
            else:
                print('A crash happened!')
                print(f'{car} was hit at {car[current_green + free_window]}.')
                crashed = True
                break
            current_green -= len(car)
    else:
        cars.append(line)

if not crashed:
    print('Everyone is safe.')
    print(f'{passed_counter} total cars passed the crossroads.')

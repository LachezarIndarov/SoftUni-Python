"""
input1
Game of Thrones
60
96

output1
You have enough time to watch Game of Thrones and left with 0 minutes free time.

input2
Teen Wolf
48
60

output2
You don't have enough time to watch Teen Wolf, you need 11 more minutes.

"""
#GitHub  - 100% Judge

from math import ceil

series_name = str(input())
episode_duration = int(input())
duration_of_the_rest = int(input())


time_for_lunch = duration_of_the_rest / 8
time_for_rest = duration_of_the_rest / 4
time_left = duration_of_the_rest - time_for_lunch - time_for_rest


if episode_duration > time_left:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_duration - time_left)} more minutes.")
else:
    print(f'You have enough time to watch {series_name} and left with {ceil(time_left - episode_duration)} minutes free time.')


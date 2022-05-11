"""
input1
10464
1500
20

output1
No, he failed! He was 20786.00 seconds slower.

input2
55555.67
3017
5.03

output2
Yes, he succeeded! The new world record is 17688.01 seconds.
"""
#GitHub  - 100% Judge

from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_second_for_meter = float(input())


ivan_has_to_swim = distance_in_meters * time_second_for_meter

water_resistance = floor(distance_in_meters / 15) * 12.5

total_time = ivan_has_to_swim + water_resistance

check_world_record = total_time - record_in_seconds

if total_time >= record_in_seconds:
    print(f"No, he failed! He was {abs(check_world_record):.2f} seconds slower.")

elif total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")





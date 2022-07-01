"""
input1
march
3
3
day

output1
Price per person for one hour: 10.50
Total cost of the visit: 94.50

input2
july
5
5
night

output2
Price per person for one hour: 4.59
Total cost of the visit: 114.75

"""

months = str(input())
the_number_of_hours_spent = int(input())
the_number_of_people_in_the_group = int(input())
the_time_of_day = str(input())

day = 0
night = 0

if months == "march" or months == "april" or months == "may":

    if the_time_of_day == "day":
        day = 10.50
        if the_number_of_people_in_the_group >= 4:
            day -= day * 0.1
        if the_number_of_hours_spent >= 5:
            day -= day * 0.5

        total_cost = (day * the_number_of_people_in_the_group) * the_number_of_hours_spent
        print(f"Price per person for one hour: {day:.2f}")

    elif the_time_of_day == "night":
        night = 8.40
        if the_number_of_people_in_the_group >= 4:
            night -= night * 0.1
        if the_number_of_hours_spent >= 5:
            night -= night * 0.5
        total_cost = (night * the_number_of_people_in_the_group) * the_number_of_hours_spent
        print(f"Price per person for one hour: {night:.2f}")

elif months == "june" or months == "july" or months == "august":

    if the_time_of_day == "day":
        day = 12.60
        if the_number_of_people_in_the_group >= 4:
            day -= day * 0.1
        if the_number_of_hours_spent >= 5:
            day -= day * 0.5
        total_cost = (day * the_number_of_people_in_the_group) * the_number_of_hours_spent
        print(f"Price per person for one hour: {day:.2f}")

    elif the_time_of_day == "night":
        night = 10.20
        if the_number_of_people_in_the_group >= 4:
            night -= night * 0.1
        if the_number_of_hours_spent >= 5:
            night -= night * 0.5
        total_cost = (night * the_number_of_people_in_the_group) * the_number_of_hours_spent
        print(f"Price per person for one hour: {night:.2f}")



print(f"Total cost of the visit: {total_cost:.2f}")


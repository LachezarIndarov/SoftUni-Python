"""
input1
May
15

output1
Apartment: 877.50 lv.
Studio: 525.00 lv.

input2
June
14

output2
Apartment: 961.80 lv.
Studio: 1052.80 lv.

input3
August
20

output3
Apartment: 1386.00 lv.
Studio: 1520.00 lv.

"""
#GitHub  - 100% Judge

month = str(input())
number_of_nights = int(input())

studio = 0
apartment = 0

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65

    studio = studio_price * number_of_nights
    apartment = apartment_price * number_of_nights

    if number_of_nights > 7 and number_of_nights <= 14:
            studio -= studio * 0.05
    elif number_of_nights > 14:
            studio -= studio * 0.3
            apartment -= apartment * 0.1

elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.70


    studio = studio_price * number_of_nights
    apartment = apartment_price * number_of_nights

    if number_of_nights > 14:
        studio -= studio * 0.2
        apartment -= apartment * 0.1

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

    studio = studio_price * number_of_nights
    apartment = apartment_price * number_of_nights

    if number_of_nights > 14:
           apartment -= apartment * 0.1


print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")







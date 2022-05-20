"""
input1
50
summer

output1
Somewhere in Bulgaria
Camp - 15.00

input2
75
winter

output2
Somewhere in Bulgaria
Hotel - 52.50

input3
312
summer

output3
Somewhere in Balkans
Camp - 124.80

input4
1500
summer

output4
Somewhere in Europe
Hotel - 1350.00

"""
#GitHub  - 100% Judge

budget = float(input())
season = str(input())

destination = ""
sleep = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget -=  budget * 0.70
        sleep = "Camp"
    elif season == "winter":
        budget -= budget * 0.30
        sleep = "Hotel"

if budget <= 1000 and budget > 100:
    destination = "Balkans"
    if season == "summer":
        budget -= budget * 0.60
        sleep = "Camp"
    elif season == "winter":
        budget -= budget * 0.20
        sleep = "Hotel"

if budget > 1000:
    destination = "Europe"
    if season == "summer":
        budget -= budget * 0.10
        sleep = "Hotel"
    elif season == "winter":
        budget -= budget * 0.10
        sleep = "Hotel"


print(f"Somewhere in {destination}")
print(f"{sleep} - {(budget):.2f}")



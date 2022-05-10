"""
input1
20000
120
55.5

output1
Action!
Wingard starts filming with 11340.00 leva left.

input2
15437.62
186
57.99

output2
Action!
Wingard starts filming with 4186.33 leva left.

input3
9587.88
222
55.68

output3
Not enough money!
Wingard needs 2495.77 leva more.

"""
#GitHub  - 100% Judge

movie_budget = float(input())
number_people = int(input())
price_for_clothing = float(input())

sum_for_decor =  movie_budget * 0.1
sum_for_clothing = number_people * price_for_clothing

if number_people > 150 :
    discount = sum_for_clothing * 0.1
    sum_for_clothing = sum_for_clothing - discount



all_sum_movie = sum_for_decor + sum_for_clothing

if all_sum_movie > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {all_sum_movie - movie_budget:.2f} leva more.")
    
elif movie_budget >= all_sum_movie:
    print(f"Action!")
    print(f"Wingard starts filming with {(movie_budget - all_sum_movie):.2f} leva left.")







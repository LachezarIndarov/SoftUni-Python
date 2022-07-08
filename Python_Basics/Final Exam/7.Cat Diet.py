"""
input1
60
25
15
2500
60

output1
2.4000

input2
40
40
20
3000
40

output2
3.0857

input3
20
60
20
1800
50

output3
2.2500

"""
fat_percentage = int(input())
percentage_of_proteins = int(input())
percentage_of_carbohydrates = int(input())
total_calories = int(input())
percentage_water = int(input())



total_fat_grams = ((fat_percentage * total_calories) / 100) / 9              #(60 % от 2500) / 9
total_proteins_grams = ((percentage_of_proteins * total_calories) / 100) / 4             #(25 % от 2500) / 4
total_carbohydrates_grams = ((percentage_of_carbohydrates * total_calories) / 100) / 4    #(15 % от 2500) / 4

the_weight_of_the_food = total_fat_grams + total_proteins_grams + total_carbohydrates_grams
calories_per_gram_of_food = total_calories / the_weight_of_the_food

#!!!!!!!  (1 - percentage_water / 100) = 1 - 60/100 = 1 - 0.6 = 0.4
one_gram_of_this_type_of_food = calories_per_gram_of_food * (1 - percentage_water / 100)

print(f"{one_gram_of_this_type_of_food:.4f}")


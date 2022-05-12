"""
input1
900
2
1
3

output1
You have 198.75 leva left!

input2
920.45
3
1
1

output2
Not enough money! You need 3.92 leva more!

"""
#GitHub  - 100% Judge

budget_Petar = float(input())
amount_video_cards = int(input())
amount_CPU = int(input())
amount_RAM = int(input())


video_card_price = 250
video_card_full_price = video_card_price * amount_video_cards
CPU_price = video_card_full_price * (35/100)
RAM_price = video_card_full_price * (10/100)
discount = 0

full_price_all_articles = ((video_card_price * amount_video_cards) + (CPU_price * amount_CPU) + (RAM_price * amount_RAM))



price1 = video_card_price * amount_video_cards
price2 = CPU_price * amount_CPU
price3 = RAM_price * amount_RAM

if amount_video_cards > amount_CPU:
    discount = full_price_all_articles * (15 / 100)


final_price = (budget_Petar - (full_price_all_articles - discount))

if budget_Petar >= full_price_all_articles:
    print(f"You have {(final_price):.2f} leva left!")

elif budget_Petar < full_price_all_articles:
    print(f"Not enough money! You need {abs(final_price):.2f} leva more!")





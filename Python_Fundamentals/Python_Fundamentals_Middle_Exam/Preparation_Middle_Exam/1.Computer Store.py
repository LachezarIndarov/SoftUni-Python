insert_prices = input()
net_price = 0


while insert_prices != "special" and insert_prices != "regular":
    current_price = float(insert_prices)

    if current_price > 0:
        net_price += current_price

    else:
        print("Invalid price!")

    insert_prices = input()

if net_price <= 0:
    print("Invalid order!")
else:
    taxes = net_price * 0.2 #The taxes are 20% of each part's price you receive
    final_price = net_price + taxes


    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")

# If the customer is special, he has a 10% discount on the total price with taxes.
#    if insert_prices == "special":
#        final_price = final_price - (final_price * 0.1) #variant 2 за пресмятане на 10 % отстъпка



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#If the customer is special, he has a 10% discount on the total price with taxes.
    if insert_prices == "special":
        final_price = final_price * 0.9 # 10% discount


print(f"Total price: {final_price:.2f}$")


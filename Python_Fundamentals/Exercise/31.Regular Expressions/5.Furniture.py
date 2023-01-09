"""
Input
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase

Output
Bought furniture:
Sofa
TV
Total money spend: 2436.69

Comment:
Only the Sofa and the TV are valid, for each of them we multiply the price by the quantity and print the result

"""

import re


def furniture_info():

    pattern = '>>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)'
    spend_money = 0
    product_list = []

    while True:
        data = input()

        if data == 'Purchase':
            break

        result = re.match(pattern, data)

        if result is not None:
            product = result[1]
            price = float(result[2])
            quantity = float(result[3])
            spend_money += price * quantity
            product_list.append(product)

    print('Bought furniture:')

    if spend_money > 0:
        print('\n'.join(product_list))
    print(f"Total money spend: {spend_money:.2f}")

furniture_info()




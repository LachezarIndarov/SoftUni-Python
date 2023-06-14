def shopping_cart(*args):
    dict = {
        "Soup" : 3,
        "Pizza" : 4,
        "Dessert" : 2,
    }

    products = {"Soup": [], "Pizza": [], "Dessert": []}

    for i in args:
        if i != "Stop":
            meal, product = i


            if (len(products[meal]) < dict[meal]) and (product not in products[meal]):

                products[meal].append(product)

        else:
            break



    sorted_products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))



    if any(a != [] for a in products.values()):
        result = []

        for key, value in sorted_products:
            result.append(f"{key}:")
            for el in sorted(value):
                result.append(f" - {el}")
        return "\n".join(result)

    else:
        return f"No products in the cart!"











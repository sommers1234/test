grocery_items = {"Chicken": 1.59, "Beef": 1.99, "Cheese": 1.0, "Milk": 2.5}
Shoes = {"Jordan 13": 1, "Yezzy" : 8, "Foamposite" : 10, "Air Max" : 5, "SB Dunk" : 20}



def rectangle_area(width, hieght):
    area = width * hieght
    return area

def total_price(item1, item2):
    item1_price = grocery_items[item1]
    item2_price = grocery_items[item2]
    price = item1_price + item2_price

    return price

# print("Chicken and Cheese Prices:")
# print(total_price("chicken", Cheese))  # 2.59

# print("Chicken and Cheese Price:" + str(total_price("Chicken","Cheese")))

# print("Milk and Beef Price: " + str((total_price("Milk","Beef")))


def price_difference(item1, item2):
    item1_price = grocery_items[item1] # Milk -> 2.5
    item2_price = grocery_items[item2] # Cheese -> 1.0

    if item1_price > item2_price:
        difference = item1_price - item2_price
    else:
        difference = item2_price - item1_price
        
    return difference

print(price_difference("Chicken", "Cheese"))
print(price_difference("Chicken", "Milk"))

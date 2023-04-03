print('''************************************** 
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')
       

# order = None
# counter = 0


# while order != "quit":
#     order = input("> ")
#     counter += 1
    
#     if order != "quit":
#         if counter == 1:
#             print(f"1 order of {order} has been added to your meal")
#         else:
#             print(f"{counter} obj_orders of {order} have been added to your meal")
#     else:
#         break

menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

obj_orders = {}
order = None

while order != "quit":
    order = input("> ")
    
    if order != "quit":
        item_found = False
        for category, items in menu.items():
            if order in items:
                item_found = True
                if order not in obj_orders:
                    obj_orders[order] = 1
                else:
                    obj_orders[order] += 1
        
        if item_found:
            count = obj_orders[order]
            if count == 1:
                print(f"1 order of {order} has been added to your meal")
            else:
                print(f"{count} orders of {order} have been added to your meal")
        else:
            print(f"{order} is not available in the menu. Please choose another dish")
    else:
        print(f"Your order is contain of {obj_orders} , Thank you  ")
        break


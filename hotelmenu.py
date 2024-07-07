menu={
    'Noodles':100,
    'Pasta':60,
    'Veg Rolls':70,
    'Salad':80,
    'Ice Cream':40,
}
print("Welcome to CLASSIC CUISINE Resturant")
print("Noodles:Rs100\nPasta:Rs60\nVeg Rolls:Rs70\nSalad:Rs80\nIce Cream:Rs40")
order_total = 0

item_1=input("Enter the name of item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialable")

another_order =input("Do you want to add another item?:")
if another_order == "Yes":
    item_2 = input("Enter the name of second item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaiable")

print(f"The total amount of items to pay: {order_total}")        
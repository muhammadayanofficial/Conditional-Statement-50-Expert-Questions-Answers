burger =int(input("Enter Your Burger Quantity: "))
pizza =int(input("Enter Your pizza Quantity: "))
drink =input("Do You Want Soft Drinks (Yes/No): ")

burgerPrice = burger * 500
pizzaPrice = pizza * 1200

total = burgerPrice + pizzaPrice

if drink == "Yes":
    total = total + 200

discount = 0

# Discount
if total > 5000:
    discount = 15

elif total > 3000:
    discount = 10

discount_amount = (total * discount) / 100

final_bill = total - discount_amount

print("FAST FOOD BILL")
print("Burger Bill:", burgerPrice)
print("Pizza Bill:", pizzaPrice)
print("Soft Drink:", drink)
print("Total:", total)
print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Bill:", final_bill)
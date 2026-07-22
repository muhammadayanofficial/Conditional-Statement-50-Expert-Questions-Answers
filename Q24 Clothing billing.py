customer = input("Enter Customer Name: ")
shirts = int(input("Enter Shirt Quantity: "))
pants = int(input("Enter Pant Quantity: "))
member = input("Are You A Member? (Yes/No): ")

shirt_bill = shirts * 1500
pant_bill = pants * 2500

total = shirt_bill + pant_bill

discount = 0

if total >= 10000:
    discount = 20

elif total >= 5000:
    discount = 10

if member == "Yes":
    discount += 5

discount_amount = (total * discount) / 100
final_bill = total - discount_amount

print("CLOTHING STORE BILL")
print("Customer:", customer)
print("Total:", total)
print("Discount:", discount, "%")
print("Final Bill:", final_bill)
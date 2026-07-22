name = input("Enter Customer Name: ")
units = int(input("Enter Units Consumed: "))
senior = input("Are You A Senior Citizen? (Yes/No): ")

rate = 0
bill = 0
tax = 0


if units <= 100:
    rate = 10

elif units <= 300:
    rate = 15

else:
    rate = 20
    
bill= rate * units

if senior == "Yes":
    discount = (bill * 10)/ 100
    bill = bill- discount
    
    
if bill > 5000:
     tax = (bill * 5) / 100
     bill = bill + tax
     

print("\n========== ELECTRICITY BILL ==========")
print("Customer:", name)
print("Units:", units)
print("Rate:", rate)
print("Tax:", tax)
print("Final Bill:", bill)
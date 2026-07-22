car = input("Car Type (Small/SUV): ")
service = input("Service (Normal/Premium): ")

bill = 0

if car == "Small":
    bill = 1000
else:
    bill = 1800

if service == "Premium":
    bill += 700

if bill > 2000:
    discount = (bill * 10) / 100
    bill -= discount

print("Final Bill:", bill)
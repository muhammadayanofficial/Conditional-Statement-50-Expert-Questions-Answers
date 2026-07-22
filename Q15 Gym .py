months = int(input("Enter Membership Months: "))
trainer = input("Personal Trainer (Yes/No): ")

bill = months * 2000

if months >= 12:
    discount = (bill * 20) / 100
    bill = bill - discount

elif months >= 6:
    discount = (bill * 10) / 100
    bill = bill - discount

if trainer == "Yes":
    bill = bill + 5000

print("Final Bill:", bill)


if trainer == "yes":
 print("Trainer Fee: 5000")
else:
    print("Trainer Fee: 0") 
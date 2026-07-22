cups = int(input("Enter Cups: "))
family = input("Family Pack? (Yes/No): ")

bill = cups * 250

if family == "Yes":
    bill += 1000

if cups >= 8:
    bill -= (bill * 10) / 100

print("Final Bill:", bill)
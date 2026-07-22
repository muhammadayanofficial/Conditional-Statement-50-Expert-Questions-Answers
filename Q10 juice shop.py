glasses = int(input("Juice Glasses: "))
large = input("Large Size? (Yes/No): ")

bill = glasses * 250

if large == "Yes":
    bill += glasses * 100

if glasses >= 10:
    bill -= (bill * 10) / 100

print("Final Bill:", bill)
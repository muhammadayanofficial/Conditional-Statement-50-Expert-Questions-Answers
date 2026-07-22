days = int(input("Enter Days: "))
helmet = input("Helmet? (Yes/No): ")

bill = days * 1500

if helmet == "Yes":
    bill += days * 200

if days >= 7:
    bill -= (bill * 10) / 100

print("Final Bill:", bill)
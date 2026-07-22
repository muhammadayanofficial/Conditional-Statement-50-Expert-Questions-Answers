hours = int(input("Hours Played: "))
vip = input("VIP Member? (Yes/No): ")

bill = hours * 400

if vip == "Yes":
    bill -= (bill * 10) / 100

if hours >= 5:
    bill -= (bill * 5) / 100

print("Gaming Bill:", bill)
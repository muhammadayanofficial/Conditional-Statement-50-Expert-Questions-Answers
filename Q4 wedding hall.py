guests = int(input("Enter Number of Guests: "))
decoration = input("Premium Decoration? (Yes/No): ")

bill = guests * 1000

if decoration == "Yes":
    bill += 30000

if guests >= 300:
    discount = (bill * 15) / 100
    bill -= discount

elif guests >= 150:
    discount = (bill * 10) / 100
    bill -= discount

print("\n===== WEDDING HALL =====")
print("Guests:", guests)
print("Final Bill:", bill)
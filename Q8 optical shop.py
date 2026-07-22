frame = input("Frame Type (Normal/Premium): ")
lenses = input("Anti Glare? (Yes/No): ")

if frame == "Normal":
    bill = 3000
else:
    bill = 6000

if lenses == "Yes":
    bill += 2000

if bill >= 7000:
    bill -= (bill * 10) / 100

print("Final Bill:", bill)
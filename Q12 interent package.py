package = input("Package (Basic/Standard/Premium): ")
months = int(input("Enter Months: "))

bill = 0

if package == "Basic":
    bill = months * 1000

elif package == "Standard":
    bill = months * 2000

else:
    bill = months * 3000

if months >= 12:
    discount = (bill * 15) / 100
    bill = bill - discount

print("Package:", package)
print("Final Bill:", bill)
books = int(input("Number of Books: "))
member = input("Member? (Yes/No): ")

bill = books * 800

if books >= 10:
    bill -= (bill * 10) / 100

if member == "Yes":
    bill -= (bill * 5) / 100

print("Final Bill:", bill)
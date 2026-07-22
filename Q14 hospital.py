patient = input("Enter Patient Name: ")
days = int(input("Enter Days Admitted: "))
room = input("Room Type (General/Private): ")

bill = 0

if room == "General":
    bill = days * 2000

elif room == "Private":
    bill = days * 5000

if days >= 7:
    discount = (bill * 10) / 100
    bill = bill - discount

print("Patient:", patient)
print("Final Bill:", bill)
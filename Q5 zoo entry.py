age = int(input("Enter Age: "))
camera = input("Camera? (Yes/No): ")

fee = 500

if age < 10:
    fee = 200

if camera == "Yes":
    fee += 300

print("Entry Fee:", fee)
age = int(input("Enter Your Age: "))
distance = int(input("Enter Distance (KM): "))
student = input("Are You A Student? (Yes/No): ")

fare = distance * 20

discount = 0

# Age Discount
if age < 12:
    discount = 50

elif age >= 60:
    discount = 30

# Student Discount
if student == "Yes":
    discount += 10

# Maximum Discount
if discount > 60:
    discount = 60

discount_amount = (fare * discount) / 100

final_fare = fare - discount_amount

print("BUS FARE")
print("Distance:", distance, "KM")
print("Original Fare:", fare)
print("Discount:", discount, "%")
print("Final Fare:", final_fare)
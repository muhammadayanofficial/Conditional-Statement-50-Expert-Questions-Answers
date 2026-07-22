age = int(input("Enter Age: "))
weight = int(input("Enter Weight (kg): "))
disease = input("Any Disease? (Yes/No): ")

if age >= 18 and weight >= 50 and disease == "No":
    print("✅ Eligible to Donate Blood")

else:
    print("❌ Not Eligible")
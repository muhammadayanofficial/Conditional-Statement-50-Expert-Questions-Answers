age = int(input("Enter Age: "))
citizen = input("Are You Pakistani? (Yes/No): ")
cnic = input("Do You Have CNIC? (Yes/No): ")

if citizen == "Yes" and cnic == "Yes" and age >= 18:
    print("Passport Application Accepted")

else:
    print("Application Rejected")
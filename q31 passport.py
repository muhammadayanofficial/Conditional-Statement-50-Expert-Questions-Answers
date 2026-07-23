age = int(input("Enter your age; "))
cnic = input("CNIC Available? (Yes/No): ")
birth = input("Birth Certificate Available? (Yes/No): ")
police = input("Police Clearance Available? (Yes/No): ")


if age >= 18:
    if cnic == "yes":
        if birth == "yes":
            if police == "yes":
                print("Approved!")
            else:
                print("Police clearance is missing")
        else:
            print("Birht Certificate Is Missing")
    else:
        print("CNIC is missing")
else:
    print("Under age")
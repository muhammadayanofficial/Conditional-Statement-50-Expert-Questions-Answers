print("Secret Laboratory")

id_card = input("Do you have an ID Card? (yes/no): ").lower()

if id_card == "yes":

    password = input("Enter Secret Password: ")

    if password == "lab123":

        fingerprint = input("Fingerprint Verified? (yes/no): ").lower()

        if fingerprint == "yes":
            print("Access Granted.")
            print("Welcome Scientist!")
        else:
            print("Fingerprint Verification Failed.")

    else:
        print("Wrong Password.")

else:
    print("ID Card Required.")
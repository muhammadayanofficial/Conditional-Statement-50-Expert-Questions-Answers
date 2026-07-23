print("Library Book Issue System")

name = input("Enter Student Name: ")
student = input("Do you have Student ID? (yes/no): ").lower()

if student == "yes":

    fine = input("Any Pending Fine? (yes/no): ").lower()

    if fine == "no":

        book = input("Is Book Available? (yes/no): ").lower()

        if book == "yes":
            print("Book Issued Successfully.")
        else:
            print("Book is not available.")

    else:
        print("Please pay your fine first.")

else:
    print("Student ID Required.")
print(" Smart Door Lock")

pin = input("Enter PIN: ")

if pin == "1234":

    fingerprint = input("Fingerprint Verified? (yes/no): ").lower()

    if fingerprint == "yes":

        face = input("Face Recognized? (yes/no): ").lower()

        if face == "yes":
            print("Door Unlocked.")
        else:
            print("Face Recognition Failed.")

    else:
        print("Fingerprint Failed.")

else:
    print("Wrong PIN.")
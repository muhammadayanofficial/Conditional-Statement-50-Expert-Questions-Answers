print("Detective Mystery")

clue = input("Did you find a clue? (yes/no): ").lower()

if clue == "yes":

    fingerprint = input("Fingerprint Found? (yes/no): ").lower()

    if fingerprint == "yes":

        suspect = input("Suspect Identified? (yes/no): ").lower()

        if suspect == "yes":
            print("Case Solved!")
        else:
            print("Find More Evidence.")

    else:
        print("No Fingerprints Found.")

else:
    print("Search the Crime Scene Again.")
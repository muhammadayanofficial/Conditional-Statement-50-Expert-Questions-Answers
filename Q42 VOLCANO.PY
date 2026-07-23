print("Volcano Rescue")

helmet = input("Helmet Available? (yes/no): ").lower()

if helmet == "yes":

    suit = input("Heat Suit Available? (yes/no): ").lower()

    if suit == "yes":

        vehicle = input("Rescue Vehicle Ready? (yes/no): ").lower()

        if vehicle == "yes":
            print("Rescue Mission Started.")
        else:
            print("Vehicle Required.")

    else:
        print("Heat Suit Missing.")

else:
    print("Helmet Required.")
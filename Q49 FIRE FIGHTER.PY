print("Firefighter Rescue")

helmet = input("Helmet Worn? (yes/no): ").lower()

if helmet == "yes":

    oxygen = input("Oxygen Mask Available? (yes/no): ").lower()

    if oxygen == "yes":

        water = input("Water Tank Full? (yes/no): ").lower()

        if water == "yes":
            print("Rescue Mission Started!")
        else:
            print("Fill the Water Tank.")

    else:
        print("Wear an Oxygen Mask.")

else:
    print("Helmet Required.")
print("Theme Park Ride")

age = int(input("Enter Age: "))
height = int(input("Enter Height (cm): "))

if age >= 12:

    if height >= 140:

        ride = input("Choose Ride (RollerCoaster/FerrisWheel): ").lower()

        if ride == "rollercoaster":
            print("Enjoy your Roller Coaster Ride!")

        elif ride == "ferriswheel":
            print("Enjoy your Ferris Wheel Ride!")

        else:
            print("Invalid Ride.")

    else:
        print("Height is too short.")

else:
    print("Age requirement not met.")
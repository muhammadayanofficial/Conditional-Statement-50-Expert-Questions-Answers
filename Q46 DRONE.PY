print("Drone Delivery")

battery = int(input("Enter Battery Percentage: "))

if battery >= 60:

    gps = input("GPS Connected? (yes/no): ").lower()

    if gps == "yes":

        weather = input("Weather Clear? (yes/no): ").lower()

        if weather == "yes":
            print("Drone Delivery Started.")
        else:
            print("Bad Weather.")

    else:
        print("GPS Connection Failed.")

else:
    print("Battery Too Low.")
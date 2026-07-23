temp1 = int(input("Enter CPU Laptop Temperature: "))
temp2 = int(input("Enter GPU Laptop Temperature: "))
fan = input("Enter Fan Speed (Low/Medium/High): ").lower()
charging = input("Charging (Yes/No): ").lower()

if temp1 >= 95 or temp2 >= 95:
    print("Shut Down Laptop")

else:

    if temp1 >= 85 or temp2 >= 85:

        if fan == "low":
            print("Increase Fan Speed")

        elif fan == "medium":
            print("Turn on Turbo Cooling")

        elif fan == "high":

            if charging == "yes":
                print("Turn on Turbo Cooling")

            else:
                print("Increase Fan Speed")

        else:
            print("Invalid Fan Speed")

    else:
        print("Everything Normal")
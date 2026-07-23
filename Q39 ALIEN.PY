print("Robot Activation")

power = input("Power On? (yes/no): ").lower()

if power == "yes":

    battery = int(input("Battery Percentage: "))

    if battery >= 50:

        command = input("Command (clean/security): ").lower()

        if command == "clean":
            print("Cleaning Started.")
        else:
            print("Security Mode Activated.")

    else:
        print("Low Battery.")

else:
    print("Robot is Off.")
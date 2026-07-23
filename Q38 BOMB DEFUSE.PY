print("Bomb Defusal")

wire = input("Choose Wire (red/blue/green): ").lower()

if wire == "red":

    timer = int(input("Time Left: "))

    if timer > 10:

        tool = input("Wire Cutter Available? (yes/no): ").lower()

        if tool == "yes":
            print("Bomb Defused!")
        else:
            print("No Wire Cutter. Mission Failed.")

    else:
        print("Too Late!")

else:
    print("Wrong Wire! Bomb Exploded.")
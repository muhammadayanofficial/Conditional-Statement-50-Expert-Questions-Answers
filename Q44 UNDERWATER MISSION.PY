print("Underwater Mission")

oxygen = int(input("Oxygen Level: "))

if oxygen >= 60:

    suit = input("Diving Suit? (yes/no): ").lower()

    if suit == "yes":

        submarine = input("Submarine Ready? (yes/no): ").lower()

        if submarine == "yes":
            print("Mission Successful.")
        else:
            print("Submarine Required.")

    else:
        print("Suit Missing.")

else:
    print("Low Oxygen.")
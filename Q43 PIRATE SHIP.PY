print("Pirate Adventure")

map = input("Treasure Map Found? (yes/no): ").lower()

if map == "yes":

    ship = input("Ship Ready? (yes/no): ").lower()

    if ship == "yes":

        crew = input("Crew Ready? (yes/no): ").lower()

        if crew == "yes":
            print("Treasure Hunt Started!")
        else:
            print("Crew Missing.")

    else:
        print("Ship Not Ready.")

else:
    print("Treasure Map Required.")
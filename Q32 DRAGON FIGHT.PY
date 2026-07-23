print("Welcome to Dragon slayer")

name = input("Enter player name: ")
health = int(input("Enter your health (hint: Health plays very very important role in this game so enter your health wisely); "))

if health >= 50:
    print("Choose your weapon")
    print("1. Sword")
    print("2. Bow")
    print("1. Magic")
    weapon = input("Enter your weapon: ")
    if weapon == "sword":
        attack = input("Choose your attact (Normal/With aura): ")
        
        if attack == "with aura":
            if health >= 70:
                print("Aura+99999 dragon can't handle your aura!")
            else:
                print("Your health and aura is too low")
                print("Dragon attacked you")
        else:
            print("You used normal attack")
            print("Dragon lost 35 health but its still alive")
            print("Now he is very angry (You're cooked)")

    elif weapon == "bow":
        attack = input("Choose your attack (Normal arrows/Fire arrows): ")
        if attack == "Fire arrows":
            if health >= 50:
                print("Nice attack you cooked the dragon with this attack but he's still standing")
            else:
                print("Your health is low!!")
        else:
            print("You used normal arrows")
            print("Dragon lost 67 Health")
    elif weapon == "magic":
        attack = input("Choose Your spell Fire (ball/Lighting strike): ")
        if attack == "Lighting strike":
            if health >= 80:
                print("You hit the dragon with lighting he is very low (5 hp)")
            else:
                print("Your health is low to used this spell")
                print("Dragon eats you")
        else:
            print("You used fire ball spell")
            print("Your burned the dragon with your spell")
            print("You won!")
            
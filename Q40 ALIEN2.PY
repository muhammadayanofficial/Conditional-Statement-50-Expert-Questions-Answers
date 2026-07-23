print("Alien Communication")

signal = input("Signal Detected? (yes/no): ").lower()

if signal == "yes":

    language = input("Translator Ready? (yes/no): ").lower()

    if language == "yes":

        peace = input("Alien Peaceful? (yes/no): ").lower()

        if peace == "yes":
            print("Communication Successful.")
        else:
            print("Run Away!")

    else:
        print("Translator Missing.")

else:
    print("No Alien Signal.")
door = input("Is the door locked? (yes/no): ").lower()
motion = input("Is motion detected? (yes/no): ").lower()
owner = input("Is the owner home? (yes/no): ").lower()

if door == "yes":

    if motion == "yes":

        if owner == "yes":
            print("Motion Detected Inside the House.")
        else:
            print("Security Notification Sent to Owner.")

    else:

        if owner == "yes":
            print("Everything is Safe.")
        else:
            print("No Action Required.")

else:

    if motion == "yes":

        if owner == "yes":
            print("Check Who Entered the House.")
        else:
            print("Alarm Triggered!")

    else:

        if owner == "yes":
            print("Reminder: Please Lock the Door.")
        else:
            print("No Action Required.")
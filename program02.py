signal = input("Enter Current Signal (red/yellow/green): ").lower()
emergency = input("Emergency Vehicle (yes/no): ").lower()
traffic = input("Traffic Density (low/medium/high): ").lower()

if emergency == "yes":

    print("Change to Green")

else:

    if signal == "green":

        if traffic == "high":

            print("Extend Green Time")

        elif traffic == "medium":

             print("Keep Signal")

        elif traffic == "low":

            print("Keep Signal")

        else:

            print("Invalid Traffic Density")

    elif signal == "yellow":

        if traffic == "high":

            print("Keep Signal")

        elif traffic == "medium":

            print("Flash Yellow Mode")

        elif traffic == "low":

             print("Flash Yellow Mode")

        else:

            print("Invalid Traffic Density")

    elif signal == "red":

        if traffic == "high":

             print("Keep Signal")

        elif traffic == "medium":

          print("Keep Signal")

        elif traffic == "low":

          print("Flash Yellow Mode")

        else:

            print("Invalid Traffic Density")

    else:

        print("Invalid Signal")
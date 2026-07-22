# 🎬 Movie Ticket Booking

age = int(input("Enter Your Age: "))
movie = input("Enter Movie Type (Action/Comedy/Horror): ")
vip = input("Do You Want VIP Seat? (Yes/No): ")

price = 0


if movie == "Horror" and age < 18:
    print("You must be 18+ to watch Horror movies.")

else:

    
    if age < 12:
        price = 500

    elif age < 60:
        price = 1000

    else:
        price = 700

    
    if vip == "Yes":
        price += 500

    print("\n Ticket Booked Successfully!")
    print("Movie:", movie)
    print("VIP Seat:", vip)
    print("Total Price: Rs.", price)
    
   
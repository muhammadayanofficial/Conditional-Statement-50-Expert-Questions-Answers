customer = input("Enter Customer Name: ")

rice = int(input("Enter Rice Bags: "))
oil = int(input("Enter Oil Bottles: "))
sugar = int(input("Enter Sugar Bags: "))

member = input("Member (Yes/No): ")
coupon = input("Do You Have Coupon (Yes/No): ")

rice_bill = rice * 3500
oil_bill = oil * 1200
sugar_bill = sugar * 1800

total = rice_bill + oil_bill + sugar_bill

discount = 0
tax = 0


if total >= 50000:
    discount = 20

elif total >= 30000:
    discount = 15

elif total >= 15000:
    discount = 10


if member == "Yes":
    discount += 5


if coupon == "Yes":
    code = input("Enter Coupon Code: ")

    if code == "SUPER50":
        discount += 5
        print("Coupon Applied")

    else:
        print(" Invalid Coupon")


if discount > 25:
    discount = 25

discount_amount = (total * discount) / 100
bill = total - discount_amount


if bill > 20000:
    tax = (bill * 5) / 100
    bill = bill + tax

if total >= 40000:
    print(" Congratulations! You Got A Free Gift Hamper.")


print("Customer Name :", customer)
print("Rice Bill     :", rice_bill)
print("Oil Bill      :", oil_bill)
print("Sugar Bill    :", sugar_bill)
print("Total Bill    :", total)
print("Discount      :", discount, "%")
print("Discount Amt  :", discount_amount)
print("Tax           :", tax)
print("Final Bill    :", bill)

name = input("Enter Customer Name: ")
balance = int(input("Enter Recharge Amount: "))
network = input("Network (Jazz/Zong/Ufone): ")
offer = input("Daily Offer? (Yes/No): ")

bonus = 0

if balance >= 1000:
    bonus = 200

elif balance >= 500:
    bonus = 100

if offer == "Yes":
    bonus += 50

print("Customer:", name)
print("Network:", network)
print("Recharge:", balance)
print("Bonus Balance:", bonus)
print("Total Balance:", balance + bonus)
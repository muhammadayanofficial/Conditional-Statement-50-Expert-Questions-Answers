course = input("Course (Python/Web/AI): ")
student = input("Are You A Student? (Yes/No): ")

fee = 0

if course == "Python":
    fee = 10000

elif course == "Web":
    fee = 12000

else:
    fee = 15000

if student == "Yes":
    discount = (fee * 15) / 100
    fee = fee - discount

print("Course Fee:", fee)
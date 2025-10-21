score = int(input("Enter score: "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else:
    print("F")
height = int(input("Enter your height in cm: "))
if height >= 120:
    age = input("Enter your age: ")
    age = int(age)
    if age < 12:
        print("Child tickets are $5")
    elif age <= 18:
        print("Youth tickets are $7")
    else:
        print("Adult tickets are $12")
else:
    print("Sorry, you have to grow taller before you can ride.")
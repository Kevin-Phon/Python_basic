print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Kids. Please pay $5.")
        bill += 5
    elif age <= 18:
        print("Youth. Please pay $7.")
        bill += 7
    else:
        print("Adult. Please pay $12.")
        bill += 12

    photo = input("Do you want to take photo(y/n): ")
    if photo == 'y':
        bill += 5
    print("Your bill is: $" + str(bill))
else:
    print("Sorry you have to grow taller before you can ride.")

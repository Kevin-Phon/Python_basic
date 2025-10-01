print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    scare = input("Do you scare(y/n): ")
    if scare == "n":
        print("You can ride the rollercoaster")
    elif scare == "n":
        print("Fucking go back, you coward.")
    else:
        print("Put only fucking y / n.")
if height < 120:
    print("Fucking too short. Go back.")

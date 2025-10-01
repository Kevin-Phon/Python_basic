print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
#pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == 'S':
    #print("Your pizza is Small Size!")
    bill += 15
    #print("Your bill now is $" + str(bill))

    pepperoni = input("\n Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == 'Y':
        #print("Added pepperoni to your pizza!")
        bill += 2
        #print("Your bill now is $" + str(bill))
    extra_cheese = input("\n Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        #print("Added extra cheese to your pizza!")
        bill += 1
        #print("Your bill now is $" + str(bill))
    print("Your final bill is: $" + str(bill) +".")

elif size == 'M':
    #print("Your pizza is Medium Size!")
    bill += 20
    #print("Your bill now is $" + str(bill))

    pepperoni = input("\n Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == 'Y':
        #print("Added pepperoni to your pizza!")
        bill += 3
        #print("Your bill now is $" + str(bill))
    extra_cheese = input("\n Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        #print("Added extra cheese to your pizza!")
        bill += 1
        #print("Your bill now is $" + str(bill))
    print("Your final bill is: $" + str(bill) + ".")

elif size == 'L':
    #print("Your pizza is Large Size!")
    bill += 25
    #print("Your bill now is $" + str(bill))

    pepperoni = input("\n Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == 'Y':
        #print("Added pepperoni to your pizza!")
        bill += 3
        #print("Your bill now is $" + str(bill))
    extra_cheese = input("\n Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        #print("Added extra cheese to your pizza!")
        bill += 1
        #print("Your bill now is $" + str(bill))
    print("Your final bill is: $" + str(bill) +".")

else:
    print("Choose only from S, M or L.")




















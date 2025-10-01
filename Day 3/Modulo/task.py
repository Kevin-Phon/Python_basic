print(10 % 3)   #1

check_number = input("Enter a number: ")
try:
    number = int(check_number)
    if number % 2 == 0:
        print("Fucking Even")
    else:
        print("Fucking Odd")
except ValueError:
        print("Put only fucking numbers")
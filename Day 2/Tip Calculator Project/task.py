# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

print("Tip calculator!")

bill = float(input("Bill: "))
tip = int(input("Tip percentage: "))
people = int(input("Number of people: "))

#calculate the final bill with tip
tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_bill = bill + total_tip_amount
print(f"The final bill is: {total_bill}")

#calculate the amount for each person with the final bill
bill_per_person = total_bill / people
print(f"Each person pays ${round(bill_per_person, 2)}")




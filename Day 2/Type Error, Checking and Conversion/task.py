#TypeError
len("Kevin")
print(len("Kevin"))

#Type Checking
print(type("Kevin"))
print(type(123))
print(type(1.23))
print(type(True))

#Type Conversion
print(float(123))
print(int(12.3))
print(str(123) + " This is not int. This is str.")
print(type(str(123)))

#print("Number of letters in your name: " + len(input("Enter your name: ")))
name = input("Enter your name: ")
length_of_name = len(name)

print("Number of letters in your name: " + str(length_of_name))

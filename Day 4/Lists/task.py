fruits = ["Cherry", "Apple", "Pear"]

print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[-1])

fruits[1] = "orange"    # change position1 value to orange
print(fruits)

fruits.append("Apple")  # add to the last
print(fruits)

fruits.insert(1, "Banana")  # insert to given position
print(fruits)

fruits.pop(1)   # delete from given position
print(fruits)

fruits.remove("orange")
print(fruits)

fruits.reverse()
print(fruits)
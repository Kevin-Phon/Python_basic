from math import floor

bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))

print(round(bmi))

print(floor(bmi))

print(f"\nBy using f-string: ")
print(f"The original bmi is: {bmi}")
print(f"The rounded bmi is: {round(bmi)}")
print(f"The floor bmi is: {floor(bmi)}")

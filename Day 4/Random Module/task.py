import random

# # random int between 1 to 50
# rand_num = random.randint(1, 50)
# print(rand_num)
#
# # random float between 0 to 5
# rand_num2 = random.random() * 5     # 0 to 5
# print(rand_num2)
#
# # another random float by using uniform
# rand_num3 = random.uniform(0, 5)    # 0 to 5
# print(rand_num3)

coin = random.randint(1, 5)
if coin >= 1 and coin <= 2.5:
    print(coin)
    print("Head")
else:
    print(coin)
    print("Tail")
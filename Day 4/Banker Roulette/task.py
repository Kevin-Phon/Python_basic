import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# one way
random_friend = random.choice(friends)
print(random_friend)

# another way
random_index = random.randint(0, len(friends)-1)    # get a random index
print(friends[random_index])    # change that random index to value

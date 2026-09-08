import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend_number = random.randint(0, len(friends)-1)
print(friends[random_friend_number])

print(random.choice(friends))
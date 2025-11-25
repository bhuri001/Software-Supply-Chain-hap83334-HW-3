import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

# Choose a random item from a list
colors = ["red", "blue", "green", "yellow", "purple"]
random_color = random.choice(colors)
print(f"Random color: {random_color}")

# Shuffle a list randomly
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

# Generate a list of 5 random numbers between 10 and 50
random_list = [random.randint(10, 50) for _ in range(5)]
print(f"Random list of numbers: {random_list}")

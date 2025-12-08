import random

# Generate a random integer between 1 and 100 (not for crypto)  # bandit: ok
random_number = random.randint(1, 100)  # nosec B311
print(f"Random number between 1 and 100: {random_number}")

# Generate a random float between 0 and 1 (not for crypto)
random_float = random.random()  # nosec B311
print(f"Random float between 0 and 1: {random_float}")

# Choose a random color from a list (not for crypto)
colors = ["red", "blue", "green", "yellow", "purple"]
random_color = random.choice(colors)  # nosec B311
print(f"Random color: {random_color}")

# Generate a list of 5 random numbers between 10 and 50 (not for crypto)
random_list = [random.randint(10, 50) for _ in range(5)]  # nosec B311
print(f"Random list of numbers: {random_list}")

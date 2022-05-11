import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Without loops
#pw_list = []
#pw_list.extend(random.sample(letters, nr_letters))
#pw_list.extend(random.sample(symbols, nr_symbols))
#pw_list.extend(random.sample(numbers, nr_numbers))

# With loops
pw_list = []
for i in range(1, nr_letters + 1):
    pw_list.append(letters[random.randint(0, len(letters) - 1)])
for i in range(1, nr_symbols + 1):
    pw_list.append(symbols[random.randint(0, len(symbols) - 1)])
for i in range(1, nr_numbers + 1):
    pw_list.append(numbers[random.randint(0, len(numbers) - 1)])

# Randomize and output as string
random.shuffle(pw_list)
pw_final = ''.join(pw_list)
print(f"Password: {pw_final}")


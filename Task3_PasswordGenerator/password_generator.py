import random
import string

print("===== Password Generator =====")

try:
    length = int(input("Enter desired password length: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password = ""

for i in range(length):
    random_char = random.choice(all_characters)
    password += random_char

print("\nGenerated Password:", password)


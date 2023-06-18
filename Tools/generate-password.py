import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

desired_length = int(input("Enter the desired password length: "))
generated_password = generate_password(desired_length)
print("Generated password:", generated_password)
import random
import string

def generate_password(length, num_uppercase, num_lowercase, num_digits, num_special):
    uppercase_letters = ''.join(random.choices(string.ascii_uppercase, k=num_uppercase))
    lowercase_letters = ''.join(random.choices(string.ascii_lowercase, k=num_lowercase))
    digits = ''.join(random.choices(string.digits, k=num_digits))
    special_characters = ''.join(random.choices(string.punctuation, k=num_special))

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    if len(all_characters) < length:
        all_characters += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - len(all_characters)))

    password_list = random.sample(all_characters, len(all_characters))
    password = ''.join(password_list)
    return password

# Example usage
password_length = 12
num_uppercase = 2
num_lowercase = 4
num_digits = 2
num_special = 2

password = generate_password(password_length, num_uppercase, num_lowercase, num_digits, num_special)
print("Generated Password:", password)

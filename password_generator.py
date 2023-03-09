import secrets
import string

letters = string.ascii_letters
digits = string.digits
#special_characters = string.punctuation
special_characters = "!@#$%&"

alphabet = letters + digits + special_characters

password_length = 12

password = ""

for i in range(password_length):
    password += "".join(secrets.choice(alphabet))

# Insert hyphens every 3 characters
password = '-'.join([password[i:i+3] for i in range(0, len(password), 3)])

print(password)

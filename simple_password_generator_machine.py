import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def password_generator():
    PASS_LENGTH = int(input(f"What is your desired password length?"  ))

    random.shuffle(characters)
    password = []

    for x in range(PASS_LENGTH):
        rand = random.choice(characters)
        password.append(rand)

    password = "".join(password)

    print(f"Generated Password: {password}")

password_generator()
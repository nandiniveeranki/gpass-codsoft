import string
import random
def gpass(length):
    if length < 3:
        raise ValueError("Password length should be at least 3 or more ")

    lowercasel = string.ascii_lowercase
    uppercasel = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation 

    password = [
        random.choice(lowercasel),
        random.choice(uppercasel),
        random.choice(digits),
        random.choice(specials)
    ]

    total_letters = lowercasel + uppercasel+ digits + specials
    password += [random.choice(total_letters) for _ in range(length - 3)]

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the length of your password:"))

        password = gpass(length)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
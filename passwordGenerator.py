import string
import random

character = list(string.ascii_letters + string.digits + string.punctuation)

def passwordGenerator():
    length = int(input("Enter the length of the password: "))
    random.shuffle(character)
    password = []
    
    for i in range(length):
        password.append(random.choice(character))
    
    random.shuffle(password)
    password = ''.join(password)
    print(password)
    
if __name__ == '__main__':
    passwordGenerator()
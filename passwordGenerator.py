import string
import random

if __name__ == '__main__':
    
    character = list(string.ascii_letters + string.digits + string.punctuation)
       
    length = int(input("Enter the length of the password: "))
    random.shuffle(character)
    password = []
    
    for i in range(length):
        password.append(random.choice(character))
    
    random.shuffle(password)
    password = ''.join(password)
    print(password)
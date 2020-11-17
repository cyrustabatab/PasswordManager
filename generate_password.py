import random
from string import ascii_letters,digits,punctuation




def generate_password():

    number_letters = random.randint(8,10)
    number_of_digits = random.randint(2,6)
    number_of_symbols = random.randint(2,4)
    
    password = []

    for _ in range(number_letters):
        password.append(ascii_letters[random.randint(0,len(ascii_letters) - 1)])


    for _ in range(number_of_digits):
        password.append(digits[random.randint(0,len(digits) - 1)])


    for _ in range(number_of_symbols):
        password.append(punctuation[random.randint(0,len(punctuation) - 1)])

    random.shuffle(password)
    return ''.join(password)






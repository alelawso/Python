import string
import random

while True:
    #this is the initial prompt where you will ask the user how long they would like their password to be
    char_length = int(input('Please enter the number of characters for your password: '))

    numbers = string.digits #0123456789
    lower = string.ascii_lowercase #All lower case letters
    upper = string.ascii_uppercase #All Upper case letters
    symbols = string.punctuation #Special Characters

    #combines the data in one big data set
    all = numbers + lower + upper + symbols

    #creates the password with the desired character length
    password = "".join(random.sample(all, char_length))

    print(password)
    

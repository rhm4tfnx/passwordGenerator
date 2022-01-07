import colorama
import random
import string

def main(c):
    symbol = '~!@#$%^&*()_-\|{][]'
    generator = string.ascii_letters + string.digits + symbol
    result = ''.join(random.sample(generator,k=c))
    return result

length = int(input('Enter length of password : '))
print(main(length))
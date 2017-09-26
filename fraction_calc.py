from fractions import Fraction

def add(a, b):
    print('{0} + {1} = {2} '.format(a, b, a+b))

def subtract(a, b):
    print('{1} - {0} = {2}'.format(a, b, a-b))

def divide(a, b):
    print('{0} / {1} = {2}'.format(a, b, a/b))

def multiply(a, b):
    print('{0} * {1} = {2}'.format(a, b, a*b))

if __name__ == '__main__':
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Select operation - Add, Subtract, Divide, Multiply: ')
        if op == 'Add':
            add(a, b)
        if op == 'Subtract':
            subtract(a, b)
        if op == 'Divide':
            divide(a, b)
        if op == 'Multiply':
            multiply(a, b)
    except ValueError:
        print('Invalid fraction')
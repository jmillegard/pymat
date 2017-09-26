from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

if __name__ == '__main__':
    try:
        inp = input('Enter some numbers separated by whitespace: ').split(' ')
        numbers = [int(num) for num in inp]
        mean = calculate_mode(numbers)
        print('Mode of numbers is {0}'.format(mean))
    except ValueError:
        print('Invalid input')
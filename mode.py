from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])

    return modes

if __name__ == '__main__':
    try:
        inp = input('Enter some numbers separated by whitespace: ').split(' ')
        numbers = [int(num) for num in inp]
        mean = calculate_mode(numbers)
        print('Mode(s) of numbers is {0}'.format(mean))
    except ValueError:
        print('Invalid input')
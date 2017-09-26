def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N

    return mean

if __name__ == '__main__':
    try:
        inp = input('Enter some numbers separated by whitespace: ').split(' ')
        numbers = [int(num) for num in inp]
        mean = calculate_mean(numbers)
        print('Mean of numbers is {0}'.format(mean))
    except ValueError:
        print('Invalid input')
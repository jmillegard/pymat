def calculate_median(numbers):
    n = len(numbers)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(numbers)[n//2]
    else:
        return sum(sorted(numbers)[n//2-1:n//2+1])/2.0

if __name__ == '__main__':
    try:
        inp = input('Enter some numbers separated by whitespace: ').split(' ')
        numbers = [int(num) for num in inp]
        mean = calculate_median(numbers)
        print('Median of numbers is {0}'.format(mean))
    except ValueError:
        print('Invalid input')
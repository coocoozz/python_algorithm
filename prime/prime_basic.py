import math

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    odd_numbers = [n for n in range(3, num) if n % 2 == 1]
    for o in odd_numbers:
        if num % o == 0:
            return False

    return True


def prime_advanced(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    odd_numbers = [n for n in range(3, round(math.sqrt(num)+0.5)) if n % 2 == 1]
    for o in odd_numbers:
        if num % o == 0:
            return False

    return True


if __name__ == "__main__":
    total = int(input())
    data_list = list(map(int, input().split(' ')))

    count = 0
    for data in data_list:
        if prime_advanced(data):
            count += 1

    print(count)


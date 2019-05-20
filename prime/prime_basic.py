import math
import sys

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


def prime_eratosthenes(num):
    num_list = [True] * (num + 1)

    for n in range(2, (num // 2) + 1):
        if num_list[n] is True:
            num_list[n*2::n] = [False] * ((num - n) // n)

    return [i for i in range(2, num+1) if num_list[i] is True]


if __name__ == "__main__":
    test_cases = list()
    max_cases = 0
    while True:
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            break
        else:
            test_cases.append(n)
            if n > max_cases:
                max_cases = n

    prime_list = prime_eratosthenes(max_cases * 2)
    for case in test_cases:
        count = 0
        for i in range(0, len(prime_list)):
            if prime_list[i] > case and prime_list[i] <= case * 2:
                count += 1
            elif prime_list[i] > case * 2:
                break

        print(count)


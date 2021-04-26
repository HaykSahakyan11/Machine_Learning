# The Goldbach Conjecture


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def input_checker(num):
    # if num % 2 == 0 and 2 < num <= 10000:
    #    return True
    # else:
    #    return False
    return True if num % 2 == 0 and 2 < num <= 10000 else False


def goldbach(num):
    data_is_correct = input_checker(num)
    if data_is_correct:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                return print(i, num - i, sep=" ")
    else:
        print("Wrong Input")


goldbach(num=int(input()))

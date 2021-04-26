# Palindrome numbers


def is_palindrome_num(num):
    if str(num) == str(num)[::-1]:
        return True
    return False


def palindrome_numbers(a, b):
    for i in range(a, b + 1):
        if is_palindrome_num(i):
            print(i, end=" ")


palindrome_numbers(a=int(input("Num1 ")), b=int(input("Num2 ")))

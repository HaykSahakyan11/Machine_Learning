# Lucky Numbers


def is_lucky_num(num):
    odd = 0
    even = 0
    for i in range(-1, -len(num), -2):
        odd += int(num[i])
        even += int(num[i - 1])
    if len(num) % 2 == 1:
        odd += int(num[0])
    return odd == even


# version 1 (my)
# print("Yes" if is_lucky_num(input("Num ")) else "No")

def is_lucky_num_2(n):
    odd = 0
    even = 0
    parity = 1
    while n > 0:
        if parity:
            odd += n % 10
        else:
            even += n % 10
        parity = 1 - parity
        n //= 10
    return even == odd


# print("Yes" if is_lucky_num_2(int(input("Num "))) else "No")


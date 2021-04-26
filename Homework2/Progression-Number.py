# Progression-Number
n = int(input())

is_arithm_progression = True

# d --> delta or difference
d = (n % 10) - (n // 10) % 10

# cause we know "d" we can remove last digit
n = n // 10

while n // 10:
    last_dig = n % 10
    pre_last_dig = (n // 10) % 10
    if last_dig - pre_last_dig != d:
        is_arithm_progression = False
        break
    n //= 10

if is_arithm_progression:
    print("Yes")
else:
    print("No")

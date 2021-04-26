# Dual Numbers
n = int(input())
dig_1 = 'Empty'
dig_2 = 'Empty'
is_dual = True

# number is dual when it < 101
if n <= 101:
    n //= 101

# otherwise
while n:
    digit = n % 10
    if dig_1 == 'Empty':
        dig_1 = digit
    elif dig_2 == 'Empty' and digit != dig_1:
        dig_2 = digit
    elif digit != dig_1 and digit != dig_2:
        is_dual = False
        break
    n //= 10

if is_dual:
    print("Dual")
else:
    print("Not Dual")

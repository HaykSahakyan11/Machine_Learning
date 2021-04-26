# Suffix Sums

a_list = list(map(float, input().split()))
_sum = sum(a_list)
while a_list:
    print(_sum, end=" ")
    _sum -= a_list.pop(0)

def is_monoton(num):
    is_asc = True
    is_desc = True
    for i in range(1, len(num)):
        if num[i] <= num[i - 1]:
            is_asc = False
        if num[i] >= num[i - 1]:
            is_desc = False

    if is_asc:
        return "Ascending"
    if is_desc:
        return "Descending"
    return "Neither"


num = list(map(int, input().split()))
# num = [int(x) for x in input().split()]
print(is_monoton(num))

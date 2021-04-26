# Cyclic shift

N = int(input())
k = int(input())

a_list = list(map(int, input().split()))

k %= N

print(a_list[N - k:] + a_list[:N - k])

# for just values
# print(*a_list[N - k:] + a_list[:N - k])

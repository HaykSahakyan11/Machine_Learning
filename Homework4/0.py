from collections import Counter

def icecreamParlor(m, arr):
    costs = Counter(arr)
    half = m/2
    combos = set()
    for cost in costs:
        if (cost!=half and m-cost in costs) or (cost==half and costs[cost]>1):
            combos.add(cost)
    for index,cost in enumerate(arr,1):
        if cost in combos:
            yield index
for _ in range(int(input())):
    m,n = int(input()), int(input())
    arr = list(map(int,(input().split())))
    print(*icecreamParlor(m, arr))
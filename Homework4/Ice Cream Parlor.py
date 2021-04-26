def whatFlavors(cost, money):
    half = money / 2
    rev_cost = cost[::-1]

    for i in range(len(cost)):
        if cost[i] != half and money - cost[i] in cost:
            return print(
                f"{i + 1}"
                f" {cost.index(money - cost[i]) + 1}"
            )
        elif cost[i] == half and \
                i != abs(rev_cost.index(cost[i]) - len(cost) + 1):
            return print(
                f"{i + 1}"
                f" {abs(rev_cost.index(cost[i]) - len(cost))}"
            )


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
        #ooo(cost, money)


#def whatFlavors(cost, money):
#    cost_dict = {}
#    for i, c in enumerate(cost):
#        if money - c in cost_dict:
#            res = f'{(cost_dict[money - c] + 1)} {i + 1}'
#            return res
#
#        cost_dict[c] = i

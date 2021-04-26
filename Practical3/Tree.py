def print_tree(n):
    space = (n - 1) // 2
    star = 1

    while star <= n:
        print("{}{}{}".format(" " * space, "*" * star, " " * space))
        space -= 1
        star += 2


print_tree(7)

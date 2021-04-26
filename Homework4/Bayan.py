def bayan():
    num = int(input("Number of stores "))
    stores = set()

    for i in range(num):
        store = input("Store {} ".format(i + 1))
        stores.add(store)
    return print(num - len(stores))


bayan()

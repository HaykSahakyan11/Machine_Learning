a_list = [1, 2, 3, 1, 1, 3]
a_dict = {}


def factor(num):
    output = 1
    a = 2
    b = num -2
    for i in range(len(num)+1):
        output *= i

uu = {}
for i in a_list:
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1

    uu[i] = uu.get(i,0) + 1


for key, value in a_dict.items():
    if value >1:
        pass


print(a_dict)

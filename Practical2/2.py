# Boring Numbers
# num = int(input())
# # digit = None
# #
# # if not num:
# #     print("Boring")
# #
# # while num:
# #     if digit is None:
# #         digit = num % 10
# #     else:
# #         if digit != num % 10:
# #             print("Intersting")
# #             break
# #         else:
# #             if num // 10 == 0:
# #                 print("Boring")
# #                 break
# #             num //= 10



# Largest Number

num = int(input())
possible = False

first_n = num // 10


while num // 10:
    print(first_n, "lllllllllll")
    if first_n != num // 10:
        possible = True
        break
    num //= 10

if possible:
    print("Yes")
else:
    print("No")

#x = input()
#if (x.isdigit()):
#    for i in range(len(x)):
#        m = i + 1
#        if i == len(x) - 1:
#            print('No')
#            break
#        elif int(x[i]) < int(x[m]):
#            print('yes')
#            break
#        else:
#            for m in range(len(x)):
#                m = i + 1
#                if int(x[i]) < int(x[m]):
#                    print('Yes')
#                    break
#                break
#else:
#    print('Incorrect input')

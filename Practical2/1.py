# Salaries
emp_1 = int(input())
emp_2 = int(input())
emp_3 = int(input())
top = None
lowest = None

# if emp_1 >= emp_2 >= emp_3:
#     top = emp_1
#     lowest = emp_3
#
# if emp_1 >= emp_3 >= emp_2:
#     top = emp_1
#     lowest = emp_2
#
# if emp_3 >= emp_1 >= emp_2:
#     top = emp_1
#     lowest = emp_2
#
# print(top - lowest)
#
# if emp_1 > emp_2:
#     top = emp_1
#     if emp_2 > emp_3:
#         lowest = emp_3
#     else:
#         lowest = emp_2
# else:
#     if emp_2 > emp_3:
#         top = emp_2
#         if


if emp_1 < emp_2:
    top = emp_2
    lowest = emp_1
    emp_1 , emp_2 = emp_2 , emp_1
if emp_1 < emp_3:
    top = emp_1
    lowest = emp_3
    emp_1, emp_3 = emp_3, emp_1

if emp_3 < emp_2:
    top = emp_2
    lowest = emp_3
    emp_2, emp_3 = emp_3, emp_2

print(emp_1 - emp_2)
print(top)
print(lowest)


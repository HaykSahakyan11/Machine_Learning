def minimumNumber(n, password):
    count = 0


    if not any(i.isdigit() for i in password):
        count += 1
    if not any(i.islower() for i in password):
        count += 1
    if not any(i.isupper() for i in password):
        count += 1
    if not any(i in '!@#$%^&*()-+' for i in password):
        count += 1
    return max(count, 6 - n)






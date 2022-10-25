def prime_number_checker(i):
    for x in range(2,i):
        if (i % x) == 0:
            break
    else:
        return i


def fancy_numnum(s):
    for i in range(len(s)-2):
        if s[i] == '7' and s[i+1] == '7' and s[i+2] == '7':
            return True


list = []
for m in range(1,100000):
    if prime_number_checker(m) == m:
        list.append(m)

#print(list)
amount = 0
for x in list:
    x = str(x)
    if fancy_numnum(x) == True:
        print(x)
        amount += 1

print(amount)


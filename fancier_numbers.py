from itertools import product
from math import sqrt
#HOPEFULLY IMPROVED
def generating_numbers(k):
    list1 = [0,1,2,3,4,5,6,7,8,9]
    comb = []
    for x in product(list1, repeat = k):
        x_1 = (''.join(map(str,x)))
        comb.append(x_1)
    return comb


def fancy_factor(fancy_number,k):
    list2 = []
    for x in comb_1:
        fancy_num = x + fancy_number
        list2.append(fancy_num)
        list2.append(fancy_num[::-1])
        slice1 = fancy_num[:k - 1]
        slice2 = fancy_num[k - 1]
        fancy_num = slice1 + fancy_number + slice2
        list2.append(fancy_num)
        list2.append(fancy_num[::-1])
    for i in list2:
        if i[0] == '0':
            list2.remove(i)
    return list2


def prime_number_checker(comb_2):
    amount = 0
    for i in comb_2:
        i = int(i)
        for x in range(2,int(sqrt(i) + 1)):
            if (i % x) == 0:
                amount += 1
                break
    amount_of_primes = len(comb_2) - amount
    return amount_of_primes

comb_1 = generating_numbers(3)
comb_2 = fancy_factor('7777777',3)
comb_2 = set(comb_2)
print(prime_number_checker(comb_2))



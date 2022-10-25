from math import sqrt


def fancyfactor(fancy_factor):
    list = []
    for i in range(1,10):
        for j in range(0,10):
            for x in range(0,10):
                fancy_number = str(i) + str(j) + str(x) + fancy_factor
                list.append(int(fancy_number))

    for i in range(1,10):
        for j in range(0,10):
            for x in range(0,10):
                fancy_number = fancy_factor + str(i) + str(j) + str(x)
                list.append(int(fancy_number))

    return list


def fancierfactor(fancy_factor):
    list2 = []
    for i in range(1,10):
        for j in range(0,10):
            for x in range(0,10):
                fancier_number = str(i) + fancy_factor + str(j) + str(x)
                list2.append(int(fancier_number))

    for i in range(1, 10):
        for j in range(0, 10):
            for x in range(0, 10):
                fancier_number = str(i) +  str(j) + fancy_factor + str(x)
                list2.append(int(fancier_number))

    return list2


a = fancyfactor('7777777')
b = fancierfactor('7777777')
all_the_right_numbers = a + b


def prime_number_checker(all_the_right_numbers):
    amount = 0
    for i in all_the_right_numbers:
        for x in range(2,int(sqrt(i) + 1)):
            if (i % x) == 0:
                amount += 1
                break
    amount_of_primes = len(all_the_right_numbers) - amount
    return amount_of_primes

print(prime_number_checker(all_the_right_numbers))

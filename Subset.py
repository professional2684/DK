# -*- coding: utf-8 -*-

from itertools import combinations

def isPrime(val):
    status = True

    if val %2 == 0 and val != 2:
        status = False

    elif val > 3:
        for idx in range(2,int(val/2)+1):
            if val % idx == 0:
                status = False
                break

    return status

def findSubSet(inarr):
    pr_sum = 0
    max_count = 0
    max_val = inarr[0]
    max_num = inarr[1]
    temp_dict = {}

    if max_val > 1:
        pr_set = [n for n in range(2, max_val) if isPrime(n)]

        for n in range(1, len(pr_set)+1):
            # pr_sum += sum([1 for x in combinations(pr_set,n) if isPrime(sum(x))])

            temp_dict = {max(n) : n for n in combinations(pr_set,n) if isPrime(sum(n))}
            max_count += sum([1 for key, val in temp_dict.items() if key < max_num])

            pr_sum += len(temp_dict)

    print(pr_sum, max_count)

# k = int(input())
# n = list(map(int, input().split(' ')))

k = 2
n = [10,1]

findSubSet(n)

# print(isPrime(8))
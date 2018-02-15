#!/bin/python3

import sys
import math

def sq_root(nos):

    sq_root_nrst = sq_min(nos)
    sq_root_nrst_ma = max_sqroot(nos)
    for nums in range(sq_root_nrst,sq_root_nrst_ma):
        square=nums*nums
        #print(square)
        str_square=int(''.join(list(str(square))[0::2]))
        nostr=''
        for no in nos:
            nostr = nostr+ str(no)
            nums_no = int(nostr)
        if (nums_no==str_square) and (math.sqrt(square).is_integer()):
            return int(math.sqrt(square))






    return 0


def max_sqroot(nos):
    nostr1 = ''
    for no in nos:
        nostr1 = nostr1 + '9' + str(no)
    sqre_nearest_ma = int(nostr1)
    sq_root_nrst_ma = int(math.sqrt(sqre_nearest_ma))
    return sq_root_nrst_ma


def sq_min(nos):
    nostr = ''
    for no in nos:
        nostr = nostr + '0' + str(no)
    sqre_nearest = int(nostr)
    sq_root_nrst = int(math.sqrt(sqre_nearest))
    return sq_root_nrst


if __name__ == "__main__":
    n = int(input().strip())
    numbers = list(map(int, input().strip().split(' ')))
    result = sq_root(numbers)
    #print (" ".join(map(str, result)))
    print(result)
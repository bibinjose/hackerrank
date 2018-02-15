#https://www.hackerrank.com/contests/w36/challenges/revised-russian-roulette
#!/bin/python3

import sys

def revisedRussianRoulette(doors):
    min=0
    counter=0
    max=(doors.count(1))
    for door in doors:
        if door==1:
            counter+=1
            if counter==2:
                counter=0
                min+=1
        else:
            counter=0

    return max-min,max

if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))



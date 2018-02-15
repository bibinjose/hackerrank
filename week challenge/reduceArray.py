
import sys

def res_fun(arr1):
    arr1.sort()
    s=0
    while(len(arr1)>1):
        arr1.sort()
        first=arr1[0]
        second=arr1[1]
        s+=first+second
        arr1 = arr1[2:]
        arr1.append(first+second)
    return s


if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = res_fun(doors)
    print (result)
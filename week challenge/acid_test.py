#https://www.hackerrank.com/contests/w36/challenges/acid-naming
#!/bin/python3

import sys

def acidNaming(acid_name):
    acid_type='not an acid'

    if(acid_name.endswith('ic') ):
        if (acid_name.startswith('hydro')):
            acid_type = 'non-metal acid'
        else:
            acid_type='polyatomic acid'
    return acid_type



if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)

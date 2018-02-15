
#!/bin/python3

import sys

def rollingString(s, operations):
  array_list=list(s)
  for op in operations:
      if op[2]=='R':
          for i in range(op[0],op[1]+1):
              if (ord(array_list[i])>121):
                  array_list[i] = 'a'
              else:
                array_list[i]=chr(ord(array_list[i]) + 1)
      else:
          for i in range(op[0],op[1]+1):
              if (ord(array_list[i])<98):
                  array_list[i] = 'z'
              else:
                  array_list[i]=chr(ord(array_list[i]) -1)
  return ''.join(array_list)

if __name__ == "__main__":
    input_str=input()
    n = int(input().strip())
    doors=[]
    for i in range(0,n):
        doors.append(list(map(str, input().strip().split(' '))))

    result = rollingString(input_str,doors)
    print (result)

#coding:utf8
import os
import sys

def fewestOperationsToBalance(s):
    m=0
    n=0
    for i in range(len(s)):
        if s[i]==')':
            if m>0:
                m=m-1
            else:
                n=n+1
        else:
            m=m+1
    if(m&n):
        return '2'
    elif m|n:
        return '1'
    else:
        return '0'

if __name__ == '__main__':
    fptr = open('1.txt', 'w')

    n = int(raw_input())

    s = raw_input()

    result = fewestOperationsToBalance(s)

    fptr.write(str(result) + '\n')

    fptr.close()


#coding:utf8

import os
import sys

def findTheAbsentStudents(n,a):
        result=[]
        for i in range(n):
            if i+1 in a:
                print str(i+1)+' not absent'
            else:
                result.append(i+1)
        return result
if __name__=='__main__':
        fptr=open('1.txt','w')
        n=int(raw_input())
        a=map(int,raw_input().rstrip().split())
        result=findTheAbsentStudents(n,a)
        fptr.write(' '.join(map(str,result)))
        fptr.write('\n')
        fptr.close()
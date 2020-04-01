#!/usr/bin/env python

import copy

a=[[1,2,3],[4,5,6],[7,8,9]]
b=a

print(a is b)
print(a==b)

a[1]='X'
print(a,b)



c=copy.copy(a)
print(a is c)
print(a==c)

a[1]=[10,11,12]
print(a,b,c)

d=copy.deepcopy(a)
print(a is d)
print(a==d)
a[1]='Z'
print(a,b,c,d)
print(dir(d))
#!/usr/bin/env python

def goldenmiddle(S):
  n=len(S)
  C=[]
  O=[]
  for i in range(0,n):
    if S[i] == '(':
      O.append(i)
    else:
      C.append(i)
  return findK(S,C,O,0,n)

def findK(S,C,O,start,end):
  numO=len([x for x in O if x in range(start,end)])
  numC=len([x for x in C if x not in range(start,end)])
  if numO == numC:
    return end
  elif numO > numC:
    end=int(end/2)
    return findK(S,C,O,0,end)
  else:
    end=int(end+end/2)
    return findK(S,C,O,0,end)

brackets= "((()))))"

print(goldenmiddle(brackets))
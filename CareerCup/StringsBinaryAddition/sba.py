#!/usr/bin/env python3

# needs review
def strbinadd(s1,s2):
  if len(s1) >= len(s2):
    bigger=s1[::-1]
    smaller=s2[::-1]
  else:
    bigger=s2[::-1]
    smaller=s1[::-1]
  lenb=len(bigger)
  lens=len(smaller)
  res=""
  up="0"
  for i in range(0,lenb):
    if i == lens:
      res+=bigger[i:lenb]
      break
    else:
      if bigger[i] == smaller[i]:
        if up == "0":
          res+="0"
        else:
          res+="1"
          up="0"
        if bigger[i] == "1":
          up="1"
      else:
        if up == "1":
          res+="0"
        else:
          res+="1"
  if up == "1":
    res+="1"

  return res[::-1]

print(strbinadd("01010","1111"))
#!/usr/bin/env python3

import collections

class Solution:
  def countLargestGroup(self, n: int) -> int:
    sum=0
    groups=collections.Counter()
    for i in range(1,n+1):
      while i // 10 != 0:
        sum+= i % 10
        i //= 10
      sum+= i % 10
      groups[sum]+=1
      sum=0
    #print(groups)
    #print(groups.most_common())
    max=0
    c=0
    for v in sorted(groups.values(),reverse=True):
      if v > max:
        max = v
        c += 1
      elif v == max:
        c += 1
      else:
        break
    return c


a=Solution()
print(a.countLargestGroup(456))
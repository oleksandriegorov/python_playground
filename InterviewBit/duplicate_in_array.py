#!/usr/bin/env python3

class Solution:
  # @param A : tuple of integers
  # @return an integer
  def repeatedNumber(self, A):
    ht = {}
    for i in A:
      if i in ht:
        return i
      else:
        ht[i] = ''
    return -1

primer=Solution()
print(primer.repeatedNumber([3,4,1,4,1]))
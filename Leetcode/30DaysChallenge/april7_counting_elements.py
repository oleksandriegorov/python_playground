#!/usr/bin/python3

# My own working of algorythm!
# Count number of occurrences for each int
# again loop through counted data and see if there is a key bigger than current one by 1
# if so - adds its count to result

from collections import Counter
from typing import List

class Solution:
  def countElements(self, arr: List[int]) -> int:
    c = Counter(arr)
    res = 0
    for i in c.keys():
      if i + 1 in c:
        res+=c[i]
    return res


a=Solution()
print(a.countElements([1,3,2,3,5,0]))
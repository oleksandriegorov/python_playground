#!/usr/bin/python3

# Again my own working!
# sort numbers and since elements may appear only once or twice - compare current and next element
# hop in 2

from typing import List
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    nums=sorted(nums)
    i=0
    while i < len(nums):
      if i == len(nums) - 1:
        return nums[i]
      elif nums[i] == nums[i + 1]:
        i += 2
      else:
        return nums[i]

a=Solution()
print(a.singleNumber([2,2,1]))
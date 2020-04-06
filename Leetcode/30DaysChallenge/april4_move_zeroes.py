#!/usr/bin/python3

from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
      newnums=len(nums)*[0]
      j=0
      if not 0 in nums:
        print(nums)
      else:
        for i in range(0,len(nums)):
          if nums[i] != 0:
            if i != j:
              nums[j]=nums[i]
              nums[i]=0
            j+=1
        print(nums)


a=Solution()
a.moveZeroes([1,1,0,3,12,4])
a.moveZeroes([1,0,1])

#!/usr/bin/env python3

# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

''' Idea: you can move in any direction. Therefore maximum number of steps would be a sum of biggest differences between
present and next coordinates: e.g. [0,0] to [2,3] can be done in 3 steps, because 3-0=3 > 2-0=2. Absolute value should be
used however.
'''
class Solution:
  # @param A : list of integers
  # @param B : list of integers
  # @return an integer
  def coverPoints(self, A, B):
    n = len(A)
    if n == 1:
      return 0
    i = 1
    path_len = 0
    # Assuming we start at 0.0
    last_point = [A[0],B[0]]
    while i < n:
      path_len += max(abs(A[i]-last_point[0]),abs(B[i]-last_point[1]))
      last_point=[A[i],B[i]]
      i+=1
    return path_len

primer = Solution()
print(primer.coverPoints([-7,-13],[1,-5]))
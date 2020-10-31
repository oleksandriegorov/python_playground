
# https://www.interviewbit.com/problems/add-one-to-number/

class Solution:
  # @param A : list of integers
  # @return a list of integers
  def plusOne(self, A):
    n = len(A)
    i = 0
    p = -1
    # Strip all leading zeros
    while i < n:
      if A[i] > 0:
        p = i
        break
      i+=1
    # If there are zeros only - return 1
    if p == -1:
      return [1]
    else:
      increment = True
      for i in range(n-1,p-1,-1):
        if A[i] == 9 and increment:
          A[i] = 0
          increment = True
        else:
          if increment:
            A[i]=A[i]+1
            increment = False
      if increment:
        return [1] + A[p:n+1]
      else:
        return A[p:n+1]

primer=Solution()
print(primer.plusOne([  9, 9, 9, 9, 9  ]))

#!/usr/bin/env python3

# My solution is Not Working properly

'''
Given a list of non negative integers, arrange them such that they form the largest number.
For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
'''

# non-negative
# edge cases:
  # only zeros
  # same numbers
# idea : number with a biggest highest power integer should come first - e.g. 9 vs 34 -> 9 comes first then 34, because
# 9 > 3
# brute force:
 # sort array by a value of a constant near highest power
 # if powers are the same - compare numbers:
   #
 # 9 5 34 30 3
 # 9 5 34


# 321 3 - 3213 3321
# 323 3 - 3233 3323
# 341 3 - 3413 3341

# Pad all numbers with zeros to the right to fit highest power
# compare numbers:
# 341 3
# 341 % 10 -> [1,4,3] -> element at len([1,4,3]) -1 is 3 -> sincr its len is bigger -> [1,4,3] len-2 element is 4: 4 > 3
# 3 % 10 -> [3] -> element at len([1,4,3]) - 1 is 3

class Solution:
 # @param A : tuple of integers
 # @return a strings
 def largestNumber(self, A):
  # Sort by value of a first character
  # During this sort numbers with a higher highest power value will be first
  # and followed by lower or equal powered ones
  '''
  A_sorted=sorted(A,key=lambda x:str(x)[0],reverse=True)
  n = len(A_sorted)
  result = ''
  for idx in range(0,n-1):
   if str(A_sorted[idx])[0] > str(A_sorted[idx+1])[0]:
    result+= str(A_sorted[idx])
   else:
    if len(str(A_sorted[idx])) > len(str(A_sorted[idx+1])):
     for subidx in range(1,len(str(A_sorted[idx]))):
      if str(A_sorted[idx])[subidx] > str(A_sorted[idx+1])[0]:
       result+= str(A_sorted[idx])
      else:
       if str(A_sorted[idx])[subidx] < str(A_sorted[idx+1])[0]:
        result+= str(A_sorted[idx+1])
        tmp = A_sorted[idx+1]
        A_sorted[idx+1] = A_sorted[idx]
        A_sorted[idx] = tmp
       else:
        if str(A_sorted[idx])[subidx] == str(A_sorted[idx+1])[0] and subidx == len(str(A_sorted[idx]))-1:
         result += str(A_sorted[idx])
  return result
  #n = len(A)
  #for num_idx in range(0,n):
  # for cnum_idx in range(num_idx,n):
  '''
  j = 0
  tmp =  [[] for _ in range(len(A)) ]
  for i in A:
    while i // 10 > 0:
      tmp[j].append(i%10)
      i = i // 10
    tmp[j].append(i)
    j+=1
  res = ''
  A_s = sorted(tmp,key=lambda x:x,reverse=True)
  for i in range(0,len(A_s)-1):
    n = len(A_s[i])-1
    n_plus_1 = len(A_s[i + 1])-1
    if A_s[i][n] > A_s[i+1][n_plus_1]:
      res+= ''.join(map(str,A_s[i][::-1]))
    else:
      # add a clause when N is smaller
      if n >= n_plus_1:
        for k in range(1,n):
          if A_s[k] > A_s[n_plus_1]:
            res += ''.join(map(str, A_s[i][::-1]))
          elif A_s[k] < A_s[n_plus_1]:
            #swap them and bubble smaller down
            res += ''.join(map(str,A_s[i+1][::-1]))
            t = A_s[i+1]
            A_s[i+1] = A_s[i]
            A_s[i] = t
          else:
            if A_s[k] == A_s[n_plus_1] and k == n-1:
              res += ''.join(map(str, A_s[i][::-1]))
            else:
              continue
  return res

primer=Solution()
print(primer.largestNumber([3, 30, 5, 341, 9]))
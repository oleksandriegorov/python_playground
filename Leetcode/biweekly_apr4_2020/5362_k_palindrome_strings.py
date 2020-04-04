#!/usr/bin/python3

from collections import Counter
'''
Explanation from https://leetcode.com/problems/construct-k-palindrome-strings/discuss/563379/JavaC%2B%2BPython-Straight-Forward

Condition 1. odd characters <= k
Count the occurrences of all characters.
If one character has odd times occurrences,
there must be at least one palindrome,
with odd length and this character in the middle.
So we count the characters that appear odd times,
the number of odd character should not be bigger than k.

Condition 2. k <= s.length()
Also, if we have one character in each palindrome,
we will have at most s.length() palindromes,
so we need k <= s.length().

The above two condition are necessary and sufficient conditions for this problem.
So we return odd <= k <= n
'''
class Solution:
  def canConstruct(self, s: str, k: int) -> bool:
    chars=Counter()
    for i in range(0,len(s)):
      chars[s[i]]+=1
    oddappearances=0
    for value in chars.values():
      if value % 2 != 0:
        oddappearances+=1
    if oddappearances <= k <= len(s):
      return True
    else:
      return False


a=Solution()
print(a.canConstruct('yzyzyzyz',4))
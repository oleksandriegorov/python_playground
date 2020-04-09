#!/usr/bin/python
# trick is to use stack data structure

class Solution:
  def backspaceCompare(self, S: str, T: str) -> bool:
    if S == T:
      return True
    elif S.strip('#') == T.strip('#') == '':
      return True
    else:
      ss = []
      st = []
      i = 0
      while i < len(S):
        if S[i] == '#':
          if len(ss) > 0:
            ss.pop()
        else:
          ss.append(S[i])
        i += 1
      i = 0
      while i < len(T):
        if T[i] == '#':
          if len(st) > 0:
            st.pop()
        else:
          st.append(T[i])
        i += 1

      return ss == st

a=Solution()
S="ab#c"
T="ad#c"
print(a.backspaceCompare(S,T))

s="leetcode"
# s is empty
# s is all  the same

res=''
last_appended=''
last_char=''
s=list(s)
direction=-1
while s:
  if len(s) == 1:
    res += last_appended
    res +=s[0]
    break
  if len(s) == 0:
    break
  cursor=[x for x in s if x not in last_appended]
  if not cursor:
    direction *= -1
    res += last_appended
    last_appended = ''
  elif direction == -1:
    last_char=min(cursor)
    last_appended+=last_char
    s.pop(s.index(last_char))
  elif direction == 1:
    last_char=max(cursor)
    last_appended += last_char
    s.pop(s.index(last_char))

print(res)


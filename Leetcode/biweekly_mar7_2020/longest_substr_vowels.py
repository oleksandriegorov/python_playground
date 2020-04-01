import re
def vowels_count(s):
  vowels='aeiou'
  for vowel in vowels:
    p=re.compile(r'%s'%vowel)
    f=re.findall(p,s)
    if len(f) % 2 == 1:
      return -1
  return len(s)

s='bcbcbc'
max=0
for i in range(0,len(s)):
  for j in range(1,len(s)):
    cursor = vowels_count(s[i:j+1])
    if max < cursor:
      max = cursor
print(max)

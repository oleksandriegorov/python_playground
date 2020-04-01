def solution(A):
  if max(A) < 1:
    return 1
  n = len(A)
  sortedA = sorted(set(A))
  current_min = min(sortedA)
  if current_min > 1:
    return 1
  i = current_min
  for item in sortedA:
    if item < 0:
      i = 1
    elif item != i:
      if i == 1:
        i = item + 1
      else:
        return i
    else:
      i += 1
  return i

print(solution([-9999,1,2,3,4,5,1000]))
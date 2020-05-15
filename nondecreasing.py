def check(lst):
 count = 0
 for i in range(0, len(lst)):
  if i+1 > len(lst) - 1: break
  if lst[i+1] >= lst[i]: count = count + 1
 if count == 1: return bool(True)
 else: return bool(False)

print(check([1,2,6,1,5]))

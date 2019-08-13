def findPythagoreanTriplets(nums):
  for i, numi in enumerate(nums, start=1):
   for j, numj in enumerate(nums, start=1):
       if i != j:
        for k , numk in enumerate(nums, start=1):
            if k == i or k == j:
                continue
            else:
                if numi * numi + numj * numj == numk * numk:
                  return True
  return False
print(findPythagoreanTriplets([3, 5, 12, 5, 13]))
# True

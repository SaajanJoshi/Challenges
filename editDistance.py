def Distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    distance = 0
    count = 0
    if len1 > len2:
     itterateLen = len2
    else:
     itterateLen = len1
    for i in range(0,itterateLen - 1):
        if s1[i] != s2[i]:
         count  = count + 1
         print(i, distance)
         if i -- 0:
          distance = 1 - distance
         else:
          distance = i - distance - 1
         if count == 2:
          return distance

print(Distance('biting', 'sitting'))
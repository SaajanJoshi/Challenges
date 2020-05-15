def solution(num):
 length = len(num)
 count = 0
 init = num[0]
 for i in num:
     if init < i:
      continue
 return length





print(solution([2,4,1,6,5,9,7]))
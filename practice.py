def singleNumber(nums):
    checkno = {};
    nonrepeatno = 0
    for i in nums:
        try:
            if checkno[i] > 0:
                checkno[i] = checkno[i] + 1
                if nonrepeatno == i:
                 nonrepeatno = 0
        except KeyError:
            checkno[i] = 1
            if nonrepeatno == 0:
             nonrepeatno = i
    return nonrepeatno

print(singleNumber([5, 4, 5, 10 , 4, 3,3, 2, 2]));

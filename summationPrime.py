def summationPrime(number, initial1, sum):
    initial = initial1;
    if initial > 1:
        for i in range(2, initial1):
            if (initial % i) == 0:
                initial = initial + 1;
                break;
        else:
            sum = sum + initial;
            initial = initial + 1;
    else:
        initial = initial + 1;

    if (number >=  initial):return summationPrime(number, initial, sum)
    else: return sum;


print(summationPrime(9,1,0))
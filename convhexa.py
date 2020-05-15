def to_hex(n):
    concatinateBinary = ''
    while(n >= 1):
      binaryno = int(n % 2)
      n = int(n / 2)
      concatinateBinary = concatinateBinary + str(binaryno)
    return "".join(reversed(concatinateBinary))

hexExtra = {'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}

print(to_hex(10))
print(hexExtra['10']);

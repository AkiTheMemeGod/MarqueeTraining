n = int(input())

print(n>=0 and n&(n-1)==0)
print(bin(n).count('1') == 1)
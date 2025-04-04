n = int(input())

for i in range(n):
    d = ""
    for k in range(n):
        d += chr(65+k) + " "
    print(" "*(n-i) + d)

n = int(input())
def rev(x):
    if x < 0:
        x = str(x)
        x = x[1:][::-1]
        return int(x)*-1
    if x >= 0:
        x = str(x)[::-1]
        return int(x)
print(rev(n))
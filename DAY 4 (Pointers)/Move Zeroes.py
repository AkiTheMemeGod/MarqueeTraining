
from collections import Counter
a = list(map(int, input().split()))
def f(arr):
    c = Counter(arr)
    print(c)
    z = [0] * c[0]
    o = [1] * c[1]
    t = [2] * c[1]
    return z + o + t
print(f(a))
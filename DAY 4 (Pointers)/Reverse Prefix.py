w = input("Enter a Word : ")
c = input("Enter a Character : ")
s = ""
i = w.index(c)
print(i)
length = len(w)
f = 0
r = length - 1
for _ in range(length):
    if f < i:
        s = w[f] + s
        f += 1
    elif f == i:
        pass
    else:
        s = s + w[r]
        r -= 1
s = c + s
# s = w[:i+1][::-1] + w[i+1:]
print(s)

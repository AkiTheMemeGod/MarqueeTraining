w = input("Enter a Word : ")
c = input("Enter a Character : ")
s = ""
index = w.index(c)
length = len(w)
f = 0
for i in range(0, length):
    if i <= index:
        s = w[i] + s
    else:
        s = s + w[i]

print(s)


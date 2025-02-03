x = input("Enter a 4 digit number")
l = []
for i in x:
    l.append(i)
pairs = []
for j in l:
    for i in l:
        pairs.append(int(j+i))
ans = []
for j in pairs:
    for i in pairs:
        ans.append(j+i)

new = set(ans)
print(min(list(new)))
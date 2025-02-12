strs = ["flower","flow","flight"]
sets = []
for s in strs:
    sub = 0
    i = 0
    cur = ""
    while sub <= len(s):
        cur = s[i:sub]
        if len(set(cur)) == len(cur):
            sub += 1
            sets.append(cur)
            continue
        i += 1
        sub = 0
# x = list(set(sets))
x = sets
x.sort()
print(x)
flag = ""
for i in x:
    flag = ""
    for j in strs:
        if i in j:
            flag = i
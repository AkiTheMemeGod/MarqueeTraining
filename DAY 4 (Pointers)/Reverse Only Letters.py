x = input("Enter a String : ")
x = list(x)
f = 0
r = len(x) - 1

for _ in x:
    if f > r:
        break
    if x[f].isalpha() and x[r].isalpha():
        x[f], x[r] = x[r], x[f]
        f += 1
        r -= 1
    elif x[f].isalpha():
        r -= 1
    elif x[r].isalpha():
        f += 1
x = "".join(x)
print(x)

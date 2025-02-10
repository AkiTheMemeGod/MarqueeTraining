x = input("Enter the string : ")
s = 0
for i in x:
    if i.isdigit():
        s += int(i)
    elif i == 'P':
        s += 10
    else:
        pass

print(s)


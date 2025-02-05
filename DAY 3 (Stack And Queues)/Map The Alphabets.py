alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = int(input("Enter the number: "))


result = ''
while x > 0:
    x = x - 1
    result = alph[x % 26] + result
    x = x // 26


print(result)
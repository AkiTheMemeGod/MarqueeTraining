x = int(input("Enter a number: "))

li = []

def fibonacci(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:

        return fibonacci(n-1) + fibonacci(n-2)

for i in range(x+1):
    li.append(fibonacci(i))

print(li)
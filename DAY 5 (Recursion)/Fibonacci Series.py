x = int(input("Enter a number: "))

a, b = 0, 1
print(a, end=" ")

for _ in range(1, x + 1):
    print(b, end=" ")
    a, b = b, a + b
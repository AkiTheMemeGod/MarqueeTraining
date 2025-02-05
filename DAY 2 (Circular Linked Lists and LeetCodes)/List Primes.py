def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

x = int(input("Enter the upper bound : "))
y = int(input("Enter the lower bound : "))

for i in range(x,y):
    if is_prime(i):
        count = 0
        for j in str(i):
            if is_prime(int(j)):
                count += 1
            if count == len(str(i)):
                print(i, end=", ")
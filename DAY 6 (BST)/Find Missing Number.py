x = list(map(int,input("Enter the objects of the list : ").split()))

s = sum(x)
n = x [-1]
actual_sum = n*(n+1)//2

print("The missing number in the series is  : ",actual_sum - s)


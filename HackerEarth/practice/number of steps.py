def min_steps_to_identical(n, a, b):
    # Check if it's possible to make all elements in a identical
    target = a[0]
    for i in range(1, n):
        if (a[i] - target) % b[i] != 0:
            return -1

    # Calculate the number of steps required
    steps = 0
    for i in range(n):
        if a[i] != target:
            steps += (a[i] - target) // b[i]

    return steps

# Input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output the result
result = min_steps_to_identical(n, a, b)
print(result)
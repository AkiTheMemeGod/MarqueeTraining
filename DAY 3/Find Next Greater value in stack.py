stack = [10, 20, 1, 6, 10]
final = []

for i in range(0, 5):
    if i+1 <= 4:
        if stack[i] < stack[i+1]:
            final.append(stack[i+1])
        else:
            final.append(0)
final.append(0)
print(final)

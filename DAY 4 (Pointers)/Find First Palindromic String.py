strs = list(map(str, input("Enter different Strings : ").split()))

def check(strings):
    left, right = 0, len(strings) - 1
    while left < right:
        if strings[left] != strings[right]:
            return False
        right -= 1
        left += 1
    return True

for i in strs:
    if check(i):
        print("Found a Valid Palindrome : ", i)
        break

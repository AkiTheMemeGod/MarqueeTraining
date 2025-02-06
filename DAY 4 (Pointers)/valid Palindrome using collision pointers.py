def check(strings):
    left, right = 0, len(strings) - 1
    while left < right:
        if strings[left] != strings[right]:
            return False
        right -= 1
        left += 1
    return True


x = input("Enter a phrase : ")
s = ""
for i in x:
    if i.isalnum():
        if i.isalpha():
            s = s + i.lower()
if check(s):
    print("valid palindrome")
else:
    print("not a valid palindrome")

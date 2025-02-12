s1 = "apple apple"
s2 = "banana"
s1 = s1.split()
s2 = s2.split()

i = 0
uncommons = []
if len(s1) > len(s2):
    print(s2)
else:
    while i < len(s1):
        if s1[i] != s2[i]:
            uncommons.append(s1[i])
            uncommons.append(s2[i])
        i += 1
    """return uncommons"""
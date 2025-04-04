t = input()
s = list(map(int, input().split()))
d = list(map(int, input().split()))
f = list(map(int, input().split()))
c = list(map(int, input().split()))

n = len(s)
turns = [f, c]
scores = []
for t in turns:
    su = 0

    for i in range(n):
        su += s[i] - (d[i]*t[i])
    scores.append(su)
if max(scores) == scores[0]:
    print('Flash')
else:d
    print("Cisco")
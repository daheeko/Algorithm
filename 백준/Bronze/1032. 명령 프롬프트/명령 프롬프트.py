n = int(input())
files = list()
for i in range(n):
    name = input()
    files.append(name)
pt = files[0]
cnt = [0 for i in range(len(pt))]
for file in files:
    for i in range(len(cnt)):
        if file[i]==pt[i]:
            cnt[i] += 1
result = ''
for i in range(len(cnt)):
    if cnt[i] == n:
        result += pt[i]
    else:
        result += '?'
print(result)

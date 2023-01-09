data = [int(input()) for _ in range(7)]
odd = [x for x in data if x%2 != 0]
if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))
import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))
count = {}

for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for num in nums:
    if num in count:
        print(count[num], end = ' ')
    else:
        print(0, end = ' ')
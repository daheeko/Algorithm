import sys
input = sys.stdin.readline

N = int(input())
nums = [int(n) for n in input().rstrip().split()]
print(min(nums), max(nums))

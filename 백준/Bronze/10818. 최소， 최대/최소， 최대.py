import sys
input = sys.stdin.readline

N = int(input())
nums = [int(n) for n in input().rstrip().split()]
nums.sort()
print(nums[0], nums[-1])

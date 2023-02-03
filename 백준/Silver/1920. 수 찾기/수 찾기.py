from bisect import bisect_left, bisect_right

def count_by_range(array, right, left):
    right_idx = bisect_right(array, right)
    left_idx=  bisect_left(array, left)
    return right_idx - left_idx


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in b:
    if count_by_range(a, i, i) == 0:
        print(0)
    else:
        print(1)
    
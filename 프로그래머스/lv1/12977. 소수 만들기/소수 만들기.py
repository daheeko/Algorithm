from itertools import combinations
def is_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True
    
def solution(nums):
    result = 0
    array = list(combinations(nums, 3))
    for arr in array:
        sum_arr = sum(arr)
        if is_prime(sum_arr):
            result += 1
    return result
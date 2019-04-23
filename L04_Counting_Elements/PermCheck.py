# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training7UEKAA-TV9/

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    nums = set([i for i in range(1, n+1)])
    for num in A:
        if num in nums:
            nums.remove(num)
        else:
            return 0
    return 1 if len(nums) == 0 else 0
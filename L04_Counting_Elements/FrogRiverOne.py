# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingWREQUC-CKY/

def solution(X, A):
    # write your code in Python 3.6
    nums = set([i for i in range(1, X+1)])
    for i, num in enumerate(A):
        if num in nums:
            nums.remove(num)
            if len(nums) == 0:
                return i
    return -1
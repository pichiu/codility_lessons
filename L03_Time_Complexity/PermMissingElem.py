# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingUVR6Q5-PEJ/

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    nums = set([i for i in range(1, n+2)])
    for num in A:
        nums.remove(num)
    return nums.pop()
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training9QTF9R-SHK/

def solution(A):
    # write your code in Python 3.6
    nums = sorted([num for num in A if num > 0])
    prev = 0
    for num in nums:
        if num - prev > 1:
            return prev + 1
        prev = num
    return prev + 1
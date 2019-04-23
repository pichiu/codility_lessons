# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingWM9RQV-XC7/

def solution(A):
    # write your code in Python 3.6
    if len(A) == 3:
        return A[0] * A[1] * A[2]
    A.sort()
    
    if A[-1] <= 0:
        return A[-1] * A[-2] * A[-3]
    elif A[-3] <= 0:
        return A[0] * A[1] * A[-1]
    else:
        return A[-1] * max(A[0] * A[1], A[-2] * A[-3])
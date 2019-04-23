# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingWQ5KKQ-GZ4/

def solution(A, K):
    # write your code in Python 3.6
    n = len(A)
    k = K % n
    if k == 0:
        return A
    else:
        return A[-k:] + A[:-k]
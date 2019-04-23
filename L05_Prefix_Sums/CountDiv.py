# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingZHUW6K-VVH/

def solution(A, B, K):
    # write your code in Python 3.6
    small, large = A // K, B // K
    ret = large - small
    if A % K == 0:
        ret += 1
    return ret
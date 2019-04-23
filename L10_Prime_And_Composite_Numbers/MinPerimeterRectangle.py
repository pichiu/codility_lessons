# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training2MXSTZ-4FE/

def solution(N):
    # write your code in Python 3.6
    i, ret = 1, float('inf')
    while i * i < N:
        if N % i == 0:
            ret = min(ret, 2 * (i + (N // i)))
        i += 1
    if i * i == N:
        ret = min(ret, 2 * (i + i))
    return ret
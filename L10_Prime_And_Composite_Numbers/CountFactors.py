# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training8FRKG5-59H/

def solution(N):
    # write your code in Python 3.6
    i, ret = 1, 0
    while i * i < N:
        if N % i == 0:
            ret += 2
        i += 1
    if i * i == N:
        ret += 1
    return ret
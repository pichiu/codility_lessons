# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingPY35RF-RRQ/

def solution(N):
    # write your code in Python 3.6
    s = '{:b}'.format(N)
    prev, diff = None, 0
    for i, c in enumerate(s):
        if c == '1':
            if prev is None:
                prev = i
            else:
                diff = max(diff, i - prev - 1)
                prev = i
    return diff
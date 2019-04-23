# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingXQNU2S-YF3/

def solution(A):
    # write your code in Python 3.6
    if not A: return 0
    A.sort()
    current, count = None, 0
    for num in A:
        if num != current:
            count += 1
            current = num
    return count
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingTQ7S3N-ZU2/

def solution(A):
    # write your code in Python 3.6
    first = A[0]
    second = sum(A) - first
    n, min_diff = len(A), abs(first - second)
    for i in range(1, n-1):
        num = A[i]
        first += num
        second -= num
        min_diff = min(min_diff, abs(first - second))
    return min_diff
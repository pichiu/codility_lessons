# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingBZ72DZ-NZ9/

def solution(M, A):
    # write your code in Python 3.6
    n, front, uni, ret = len(A), 1, set(), 0
    uni.add(A[0])
    for end, num in enumerate(A):
        while front < n and A[front] not in uni:
            uni.add(A[front])
            front += 1
        ret += len(uni)
        uni.remove(num)
    return ret
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingN9A2CS-EQC/

def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    for i in range(len(A) - 2):
        if (A[i] + A[i+1] > A[i+2]) and (A[i+1] + A[i+2] > A[i]) and (A[i] + A[i+2] > A[i+1]):
            return 1
    return 0
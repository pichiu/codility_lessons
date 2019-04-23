# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingW3TM2S-YZ3/

def solution(A):
    # write your code in Python 3.6
    zero_count, ret = 0, 0
    for num in A:
        if num == 0:
            zero_count += 1
        else:
            ret += zero_count
    if ret > 1000000000:
        ret = -1
    return ret
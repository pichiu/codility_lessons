# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingTNCUCT-QA6/

def solution(A):
    # write your code in Python 3.6
    if not A: return -1
    
    size = 0
    for num in A:
        if size == 0:
            val = num
            size += 1
        elif val == num:
            size += 1
        else:
            size -=1
    cand = None
    if size > 0:
        cand = val
    
    ret = -1
    if cand is not None:
        count, first = 0, None
        for i, num in enumerate(A):
            if num == cand:
                count += 1
                if first is None:
                    first = i
        if count > len(A) // 2:
            ret = first
    return ret
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingQYQ4H2-NMG/

def solution(N, A):
    # write your code in Python 3.6
    target, max_count, cached_count = N + 1, 0, None
    d = {}
    for num in A:
        if num == target:
            cached_count = max_count
            d = {}
        else:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            max_count = max(max_count, d[num] if cached_count is None else (d[num] + cached_count))
    if cached_count is None:
        cached_count = 0
    ret = [cached_count for _ in range(N)]
    for k,v in d.items():
        ret[k-1] += v
    return ret
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingM88KG2-V2S/

def solution(N, P, Q):
    # write your code in Python 3.6
    f = [0 for _ in range(N + 1)]
    i = 2
    while i * i <= N:
        if f[i] == 0:
            k = i * i
            while k <= N:
                f[k] = i
                k += i
        i += 1
    
    t = [0 for _ in range(N + 1)]
    for i, num in enumerate(f):
        if num != 0 and f[i // num] == 0:
            t[i] = 1
    p = [0 for _ in range(N + 2)]
    for i, num in enumerate(t, 1):
        p[i] = num + p[i - 1]
        
    ret = []
    for i in range(len(P)):
        ret.append(p[Q[i] + 1] - p[P[i]])
    return ret

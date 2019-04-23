# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training5UX2UK-7JY/

def solution(S, P, Q):
    # write your code in Python 3.6
    n = len(S)
    table = [[0 for _ in range(n)] for _ in range(n)]
    d = {'A':1, 'C':2, 'G':3, 'T':4}
    
    table[0][0] = d[S[0]]
    for i, c in enumerate(S[1:], 1):
        val, prev_col = d[c], i - 1
        table[i][i] = val
        for j in range(i):
            table[j][i] = min(table[j][prev_col], val)
            
    ret = []
    for i in range(len(P)):
        ret.append(table[P[i]][Q[i]])
    return ret
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingEFYDDR-RV8/

ceil_div = lambda x, y: -(-x // y)

def solution(X, Y, D):
    # write your code in Python 3.6
    if X == Y:
        return 0
    return ceil_div(Y-X, D)
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingF5WYK4-J22/

def solution(A):
    singles = set()
    for num in A:
        if num in singles:
            singles.remove(num)
        else:
            singles.add(num)
    return singles.pop()
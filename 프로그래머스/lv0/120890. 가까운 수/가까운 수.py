def solution(array, n):
    array = sorted(array)
    answer = min(abs(i-n) for i in array)
    for i in array:
        if abs(i-n) == answer:
            return i
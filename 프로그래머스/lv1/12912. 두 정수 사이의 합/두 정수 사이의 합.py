def solution(a, b):
    answer = 0
    if a==b:
        return a
    elif a > b:
        for n in range(b, a+1):
            answer += n
        return answer
    else:
        for n in range(a, b+1):
            answer += n
        return answer
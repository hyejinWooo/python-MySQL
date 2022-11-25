def solution(n, k):
    if n >= 10:
        answer = 12000*n + 2000*k - 2000*(n//10)
    else:
        answer = 12000*n + 2000*k
    return answer
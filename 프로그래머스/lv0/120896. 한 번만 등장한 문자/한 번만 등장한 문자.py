def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
            answer = sorted(answer)
            answer = ''.join(answer)
    return answer
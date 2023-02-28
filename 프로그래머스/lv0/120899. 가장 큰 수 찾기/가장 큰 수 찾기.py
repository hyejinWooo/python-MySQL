def solution(array):
    answer = []
    for idx, i in enumerate(array):
        if i == max(array):
            answer.append(i)
            answer.append(idx)
    return answer
def solution(score):
    answer = []
    list = []
    for i in score:
        answer.append(sum(i)/2)
    answer1 = sorted(answer, reverse=True)
    for i in answer:
        list.append(answer1.index(i)+1)
    return list
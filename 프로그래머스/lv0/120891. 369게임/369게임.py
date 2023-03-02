# def solution(order):
#     answer = 0
#     for i in str(order):
#         if int(i) % 3 == 0:
#             answer += 1
#     return answer


def solution(order):
    answer = 0
    for i in str(order):
        if i in ["3", "6", "9"]:
            answer += 1
    return answer


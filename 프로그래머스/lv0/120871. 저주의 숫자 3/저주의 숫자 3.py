# def solution(n):
#     answer = 0
#     i = 1
#     while int(i) <= n:
#         if int(i) % 3 == 0:
#             i 
#             for i in str(n):
#                 answer = int(i) + 1
#     return answer

def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
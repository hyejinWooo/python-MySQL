# def solution(n):
#     answer = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#     return answer += 1

# def solution(n):
#     answer = []
#     for i in range(1,n+1):
#         if n % i == 0:
#             answer.extend([(i, n//i)])
#     return len(answer) 

def solution(n):
    answer = 0 
    for i in range(n):
        if n % (i+1) == 0:
            answer += 1
    return answer
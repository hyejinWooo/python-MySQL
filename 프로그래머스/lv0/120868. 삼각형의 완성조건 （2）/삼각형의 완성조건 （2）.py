# def solution(sides):
#     answer = 0
#     answer = sorted(sides)
#     if answer < sides[1]:
#         for i in range(0, 1001):
#             answer += i
#     return answer

def solution(sides):
    return (sorted(sides)[0] * 2) - 1
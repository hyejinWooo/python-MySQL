# def solution(before, after):
#     answer = 0
#     num = ''
#     for i in before:
#         if before.count(i) == after.count(i):
#             num += i
#         if len(num) == len(before):
#             answer == 1
#         else:
#             answer == 0
#     return answer

# def solution(before, after):
#     return 1 if sorted(before) == sorted(after) else 0 

def solution(before, after):
    answer = 0
    num = ''
    for i in before:
        if before.count(i) == after.count(i):
            num += i
    if len(num) == len(after):
        answer = 1
    else:
        answer = 0
    return answer
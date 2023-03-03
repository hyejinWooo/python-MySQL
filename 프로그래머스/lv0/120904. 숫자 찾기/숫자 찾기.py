# def solution(num, k):
#     answer = 0
#     for idx, i in enumerate(str(num)):
#         if i == k:
#             return idx + 1

def solution(num, k):
    answer = 0
    if max(list(map(int,str(num)))) < k or min(list(map(int,str(num)))) > k:
        return -1
    for i in str(num):
        answer += 1
        if i == str(k):
            break
    return answer
# def solution(str_list):
#     answer = []
#     if str_list.index < 'i':
#             answer.append(str_list[:])
#     return answer

def solution(str_list):
    answer = []
    idx=0
    for i in str_list:
        if(i=='l'):
            answer=str_list[:idx]
            break
        elif(i=='r'):
            answer=str_list[idx+1:]
            break
        idx+=1
    return answer

# l이나 r이 나올 때까지 for문 돌리기 (먼저 여부 어떻게 확인...)
# l이나 r의 인덱스 찾기
# l이나 r의 인덱스 앞이나 뒤까지 자르기
# 리스트에 추가하기
# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in ("a, e, i, o, u"):
#             answer = answer + i
#     return answer

# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in ("a, e, i, o, u"):
#             answer = answer + i
#     return answer


2
3
4
5
6
7
def solution(my_string):
    answer = ''
    for i in my_string:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            answer += i
    return answer
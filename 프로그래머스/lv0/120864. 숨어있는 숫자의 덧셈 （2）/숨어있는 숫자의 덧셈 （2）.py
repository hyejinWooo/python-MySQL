import re

def solution(my_string):
    answer = 0
    num = re.findall(r'\d+', my_string)
    for i in num:
        answer += int(i)
    return answer
# def solution(my_string, overwrite_string, s):
#     answer = my_string.replace(my_string[s:s+len(overwrite_string)], overwrite_string)
#     return answer

def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer
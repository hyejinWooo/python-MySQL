# def solution(my_string, num1, num2):
#     answer = ''
#     answer = my_string.replace(my_string[num1], my_string[num2])
#     return answer

# def solution(my_string, num1, num2):
#     s = list(my_string)
#     s[num1],s[num2] = s[num2],s[num1]
#     return ''.join(s)

def solution(my_string, num1, num2):
    my_string = list(my_string)

    temp1 = my_string[num1]
    temp2 = my_string[num2]

    my_string[num1] = temp2
    my_string[num2] = temp1

    return ''.join(my_string)
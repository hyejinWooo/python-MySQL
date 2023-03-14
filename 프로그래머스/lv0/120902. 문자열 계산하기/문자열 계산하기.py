# def solution(my_string):
#     answer = 0
#     my_string = my_string.replace(" ","").split("+")
#     for i in my_string:
#         answer += int(i)
#     return answer

# pattern = "[+-]"
# import re
# def solution(my_string):
#     answer = 0
#     my_string = my_string.replace(" ","")
#     my_string = re.split(pattern, my_string)
#     # for i in my_string:
#     #     answer += int(i)
#     return my_string

#연산자에는 + - 전부 포함...

def solution(my_string):
    answer = 0
    list = []
    my_string = my_string.split()
    for i in my_string:
        list.append(i)
    # for i in range(0, len(list)):
    #     if list[i].isdigit() == True:
    #         answer += int(list[i])
    #     if list[i] == "-":
    #         answer -= int(list[i+1])
    return list

# pattern = "[+-]"
# import re
# def solution(my_string):
#     answer = 0
#     my_string = my_string.replace(" ","")
#     my_string = re.split(pattern, my_string)
#     # for i in my_string:
#     #     answer += int(i)
#     return my_string

def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    for i in range(1, len(my_string), 2):
        if my_string[i] == "+":
            answer += int(my_string[i+1])
        else:
            answer -= int(my_string[i+1])
    return answer
import math
def solution(my_str, n):
    answer = []
    for i in range(0, math.ceil(len(my_str)/n)):
        answer.append(my_str[i*n:(i+1)*n])
#     my_str[:n]
#     my_str[n:2n]
#     my_str[2n:]
    
    return answer
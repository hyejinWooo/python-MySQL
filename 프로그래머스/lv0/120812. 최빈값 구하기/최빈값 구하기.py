# def solution(array):
#     answer = 0
#     count = []
#     for i in array:
#         a = array.count(i)
#         count.append(a)
#         print(count)
#         answer = max(count)
#         if len(array) == 1:
#             return 1
#         elif count.count(max(count)) >= 1:
#             return -1
#     return max(count)
    
def solution(array):
    answer = 0
    set_array = set(array)
    max_count = 0
    for i in set_array:
        count = array.count(i)
        if max_count < count:
            max_count = count
            answer = i
        elif max_count == count:
            answer = -1
    return answer
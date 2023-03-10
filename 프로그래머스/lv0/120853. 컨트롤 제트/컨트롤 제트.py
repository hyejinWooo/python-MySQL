def solution(s):
    answer = []
    s = s.split(' ')
    for i in range(0, len(s)):
        if s[i] != 'Z':
            answer.append(s[i])
        if s[i] == 'Z':
            answer.remove(s[i-1])
    answer = [int(i) for i in answer]
    answer = sum(answer)
    return answer

# def solution(s):
#     arr = s.split(' ')
#     result =[]
#     for i in arr :
#         if i=='Z':
#             result.pop()
#         else:
#             result.append(int(i))
#     return sum(result)

# def solution(s):
#     answer = 0
#     s = s.split(" ")
#     for i in range(1, len(s)+1):
#         if s[i] == "Z":
#             s.remove(s[i-1])
#     return s
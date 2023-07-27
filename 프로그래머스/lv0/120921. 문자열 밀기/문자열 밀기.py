def solution(A, B):
    #answer = 0
    answer = ''
    count = 0
    for i in range(-1, -len(A), -1):
        answer = A[i:] + A[:i]
        count = count + 1
        if answer == B:          
            return count
        elif A == B:
            return 0
    return -1
    #answer = A[-1] + A[:-1]
    #if answer == B:
     #   return 1
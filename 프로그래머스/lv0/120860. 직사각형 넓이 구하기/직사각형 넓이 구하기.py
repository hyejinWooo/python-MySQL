# def solution(dots):
#     x = [dot[0] for dot in dots]
#     y = [dot[1] for dot in dots]
    
#     w = max(x) - min(x)
#     h = max(y) - min(y)
#     area = w*h
#     return area

def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
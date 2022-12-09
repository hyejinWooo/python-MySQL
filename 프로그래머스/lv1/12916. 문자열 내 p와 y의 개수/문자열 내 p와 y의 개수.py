def solution(s):
    s = str.upper(s)
    if s.count("P") == s.count("Y"):
        return True
    elif s.count("P") == s.count("Y") == 0:
        return True
    else:
        return False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
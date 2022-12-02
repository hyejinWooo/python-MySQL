def solution(emergency):
    # 원본은 a라는 이름으로 가지고 있습니다.
    # emergency를 정렬한 값을 b라고 합니다.
    # a에 있는 값을 b에서 찾는데 index만 찾아서
    # 새로운 리스트로 만듭니다.
    b = sorted(emergency, reverse=True)
    
    result=[]
    for i in emergency:
        result.append(b.index(i)+1)
    return result
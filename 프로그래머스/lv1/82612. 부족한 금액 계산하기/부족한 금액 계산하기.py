def solution(price, money, count):
    pre = 0
    for i in range(1, count+1):
        pre += price*i
    if money - pre < 0:
        answer = pre - money
    else:
        answer = 0
    return answer
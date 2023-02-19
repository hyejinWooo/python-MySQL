# def solution(money: int):
#     return [money // 5500, money % 5500]

def solution(money):
    cup = money//5500
    change = money%5500
    return [cup, change]
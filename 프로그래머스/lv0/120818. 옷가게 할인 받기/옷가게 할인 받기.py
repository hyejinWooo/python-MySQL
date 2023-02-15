# def solution(price):
#     if price >= 100000 & price < 300000:
#         return price * 0.95
#     if price >= 300000 & price < 500000:
#         return price * 0.9
#     if price >= 500000:
#         return price * 0.8

def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return int(price)
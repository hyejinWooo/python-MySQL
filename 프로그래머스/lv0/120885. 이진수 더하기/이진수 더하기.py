def solution(bin1, bin2):
    answer = ''
    a = int(bin1, 2)
    b = int(bin2, 2)
    num = bin(a+b)
    answer = num[2:]
    return answer
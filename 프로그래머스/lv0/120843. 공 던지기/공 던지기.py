def solution(numbers, k):
    lists = []
    numbers = numbers * k
    for i in range(0, len(numbers), 2):
        lists.append(numbers[i])
    answer = lists[k-1]
    return answer
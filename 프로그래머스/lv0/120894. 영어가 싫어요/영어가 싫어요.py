def solution(numbers):
    answer1 = []
    answer2 = ''
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numdict = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    idx = []
    for i in num:
        if i in numbers:
            idx.append(numbers.find(i))
            idx.sort()
    for i in range(0, len(idx)-1):
        answer1.append(numbers[idx[i]:idx[i+1]])
    answer1.append(numbers[idx[len(idx)-1]:])
    for i in answer1:
        answer2 = answer2 + numdict[i]
    return int(answer2)
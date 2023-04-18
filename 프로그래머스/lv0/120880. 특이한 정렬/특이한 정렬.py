# def solution(numlist, n):
#     indexlist = []
#     answer = []
#     for i in numlist:
#         indexlist.append(numlist.index(i))
#     if numlist.index(n)
#     return indexlist

def solution(numlist, n):
    answer = []
    indexlist = []
    numlist = sorted(numlist)
    difflist = [i-n for i in numlist]
    difflist = sorted(difflist, key=abs)
    for i in range(0, len(numlist)-1):
        if difflist[i] == -difflist[i+1]:
            difflist[i], difflist[i+1] = difflist[i+1], difflist[i]
    difflist = [i+n for i in difflist]
    return difflist
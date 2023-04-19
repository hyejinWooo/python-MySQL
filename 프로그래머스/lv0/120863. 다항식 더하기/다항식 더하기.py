# import re

# def solution(polynomial):
#     answer = ''
#     xlist = []
#     numlist = []
#     newxlist = []
#     newnumlist = ''
#     polynomial = polynomial.split('+')
#     polynomial = [i.strip() for i in polynomial]
#     for i in polynomial:
#         if 'x' in i:
#             xlist.append(i)
#         if 'x' not in i:
#             numlist.append(i)
#     # for i in xlist:
#     #     newxlist.append(re.sub(r'[^0-9]', '', i))
#     for i in range(0, len(newxlist)):
#         if newxlist[i] == "":
#             newxlist[i] = '1'
#     newxlist = [int(i) for i in newxlist]
#     numlist = [int(i) for i in numlist]
#     if sum(numlist) != 0:
#         numberx = str(sum(newxlist)) + 'x + ' + str(sum(numlist))
#     else:
#         numberx = str(sum(newxlist)) + 'x'
#     return numberx

import re

def solution(polynomial):
    answer = ''
    xlist = []
    numlist = []
    newxlist = []
    newnumlist = ''
    polynomial = polynomial.split('+')
    polynomial = [i.strip() for i in polynomial]
    for i in polynomial:
        if 'x' in i:
            xlist.append(i)
        if 'x' not in i:
            numlist.append(i)
    for i in range(0, len(xlist)):
        if xlist[i] == "x":
            xlist[i] = 1
        else:
            xlist[i] = int(xlist[i].split('x')[0])
    newxlist = [int(i) for i in newxlist]
    numlist = [int(i) for i in numlist]
    if sum(xlist) != 0 and sum(xlist) != 1 and sum(numlist) != 0:
        numberx = str(sum(xlist)) + 'x + ' + str(sum(numlist))
    elif sum(xlist) == 0 and sum(numlist) != 0:
        numberx = str(sum(numlist))
    elif sum(xlist) == 1 and sum(numlist) != 0:
        numberx = 'x + ' + str(sum(numlist))
    elif sum(xlist) == 1 and sum(numlist) == 0:
        numberx = 'x'
    else:
        numberx = str(sum(xlist)) + 'x'
    return numberx
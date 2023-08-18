def solution(rank, attendance):
    dict_list= dict(zip(rank, attendance))
    # dic = dict(sorted(dict_list.items()))
    list = []
    for i in dict_list:
        if dict_list.get(i) == True:
            list.append(i)
            list = sorted(list)[:3]
    answerlist = []
    for a in list:
        answerlist.append(rank.index(a))
    answer = answerlist[0]*10000 + answerlist[1]*100 + answerlist[2]
    return answer
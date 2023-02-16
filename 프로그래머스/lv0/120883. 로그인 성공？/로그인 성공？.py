# def solution(id_pw, db):
#     if id_pw[0] == id[0] for id in db and id_pw[1] == id[1] for id in db:
#         answer = 'login'
#     elif id_pw[0] != id[0] for id in db:
#         answer = 'fail'
#     elif id_pw[0] == id[0] for id in db and id_pw[1] != id[1] for id in db:
#         answer = 'wrong pw'
#     return answer

# def solution(id_pw, db):
#     for i in db:
#         if id_pw[0] == i[0] and id_pw[1] == i[1]:
#             answer == 'login'
#         elif id_pw[0] == i[0] and id_pw[1] != i[1]:
#             answer == 'wrong pw'
#         elif id_pw[0] != id[0]:
#             answer == 'fail'
#     return answer

def solution(id_pw, db):
    for i in db:
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"
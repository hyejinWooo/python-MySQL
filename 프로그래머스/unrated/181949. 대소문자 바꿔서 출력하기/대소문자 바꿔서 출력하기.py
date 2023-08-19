str = input()
answer = ''
for i in str:
    if i.isupper() == True:
        answer = answer+i.lower()
    else:
        answer = answer+i.upper()
print(answer)
# str 형식은 append가 안 됨
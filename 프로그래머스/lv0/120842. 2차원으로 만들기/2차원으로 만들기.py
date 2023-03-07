def solution(num_list, n):
    answer = []
    for i in range(int(len(num_list)/n)):
        answer.append(num_list[i*n:(i+1)*n])
    return answer

# num_list[0:n] num_list[1n:2n] num_list[2n: 3n] num_list[3n : 4n]
# num_list[0:n] num_list[n:2n] num_list[2n:3n]
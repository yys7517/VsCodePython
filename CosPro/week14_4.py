def solution(score): 
    answer = [] 
    for i in range(len(score)) : 
        rank = 1 
        for s in score : 
            if score[i] < s : 
                rank+=1 
        answer.append(rank) 
    return answer


#score = [90,87,87,23,35,28,12,46]
score = [10,20,20,30]

ret = solution (score )
print ( ret )
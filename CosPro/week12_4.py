def solution ( votes, N , K ) :
    counter = [ 0 for _ in range(N+1) ]
    # 표 개수.
    for i in votes :
        counter[i] += 1
    # K표를 받은 후보의 수.
    count = 0

    for i in counter : 
        if i == K :
            count += 1
            
    return count


votes = [2,5,3,4,1,5,1,5,5,3]
N = 5
K = 2

print( solution(votes,N,K) )

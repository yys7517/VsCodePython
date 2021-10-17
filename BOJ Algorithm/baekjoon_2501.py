# 백준 브론즈 3 - 약수 구하기.
# N 의 약수 중 K 번째로 작은 수 출력
# K 번째 약수가 존재하지 않을 경우에는 0 출력

N,K = map( int, input().split() )
list = [] # 약수를 넣을 리스트.
for i in range ( 1, N+1 ) :
    if ( N % i == 0 ) :
        list.append( i )

if ( K > len(list) ) :
    print(0)
else :
    print( list[K-1] )
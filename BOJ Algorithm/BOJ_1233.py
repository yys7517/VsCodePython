# 백준 브론즈 2 - 주사위
# 총 3개의 주사위
# S1 = 첫 번째 주사위 면의 수
# S2 = 두 번째 주사위 면의 수
# S3 = 세 번째 주사위 면의 수

def makelist( n ) :
    returnlist = []
    for i in range ( 1, n+1 ) :
        returnlist.append(i)
    return returnlist

S1, S2, S3 = map( int, input().split() )
S1list = makelist( S1 )
S2list = makelist( S2 )
S3list = makelist( S3 )

# print(S1list)
# print(S2list)
# print(S3list)

sumlist = []
for i in S1list :
    for j in S2list :
        for k in S3list :
            sumlist.append(i + j + k)
# print("합 : ", sumlist)

# 합에 따른 개수를 담는 딕셔너리
# key = 합, value = 합 개수
countdict = {}
# 합의 경우의 수 = 최소 3 ~ S1+S2+S3
for i in range ( 3, S1+S2+S3 + 1 ) :
    countdict.update( { i : sumlist.count(i) } )

# print( "합에 따른 개수를 담는 딕셔너리 : ", countdict )

# key = 합 
key_list = list(countdict.keys())
# print("합의 종류 : ", key_list )

# values = 합 개수
countset = set ( countdict.values() )
# print("합 개수 종류 : ", countset)

# i에 키 값을 넣어서 키에 따른 값을 뽑아오면서
# max(countset) = 제일 많은 합의 개수
# 랑 비교한다. 
# key_list를 정렬하면 키 값이 오름차순이 되므로
# 제일 먼저 조건을 만족하는 i가 문제의 정답이 된다.
key_list.sort()
for i in key_list :
    if ( countdict.get(i) == max(countset) ) : 
        print(i)
        break
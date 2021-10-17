# 백준 브론즈 3 - 대회 or 인턴

# 2명의 여학생, 1명의 남학생 - 1팀
# N 여학생 수
# M 남학생 수
# K 인턴쉽 수

N,M,K = map ( int, input().split() )
count = min( N//2, M//1 )
# print(" 정해진 팀 수 : " ,count )

left = N + M - ( 3 * count )
# print(" 남은 학생 수 = ", left )

if ( left > K ) :
    print( count )
else :
    K -= left
    if ( K % 3 == 0 ) : 
        count -= K // 3
        print(count)
    else :
        count -= (K // 3) + 1
        print(count)

def one2nt_sum( n ) :
    sum = 0
    for i in range( 1, (10 * n) + 1) :
        sum += i
    return sum
N = int(input("자연수 : "))
if ( N < 1 or N > 10 ) :
    print('입력값의 범위를 초과하였습니다.')
else :
    print('1 -- ' + str(10*N) + " = ",one2nt_sum(N) )
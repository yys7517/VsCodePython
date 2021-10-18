# 정수 : 0
# 입력된 수가 0 입니다.

# 정수 : 10
# 1 -- 10 = 55

# 정수 : -10
# -1 -- -10 = -55

def one2n_sum2( n ) :
    sum = 0
    if ( n > 1 ) :
        for i in range ( 1, n+1 ) : 
            sum += i
        return sum

    else :
        # 끝 값은 - 방향으로 하나 더 크게
        for i in range ( -1, n-1, -1 ) :
            sum += i
        return sum

N = int(input("정수 : "))

if ( N == 0 ) :
    print('입력된 수가 0입니다.')
else :
    if ( N > 1 ) :
        print("1 -- " + str(N) + " = ", one2n_sum2(N) )
    else : # N < 0
        print("-1 -- " + str(N) + " = ", one2n_sum2(N) )
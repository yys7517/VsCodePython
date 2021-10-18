# 자연수를 매개변수로 전달받아 1부터 전달된 자연수까지의 합계를 구하여 반환하는 
# one2n_sum1() 함수를 선언해보자. 자연수를 입력받아 함수를 호출하고 결과를 반환받아 출력해보자.
#  단, 입력된 수가 1보다 작은 수이면 ‘입력된 수가 1보다 작습니다.’라는 문자열을 출력한다.

def one2n_sum1( n ) :
    sum = 0
    for i in range( 1, n+1 ) :
        sum += i
    return sum

N = int( input("자연수 : ") )
if ( N < 1 ) :
    print('입력된 수가 1보다 작습니다.')
else :
    print('1 -- ' + str(N) + " = " , one2n_sum1(N))



# a일장과 b일장이 같이 열리는 날이 며칠에 한 번씩 있는 지 구하는 문제
# 최소공배수를 구하는 문제
# ********유클리드 호제법******
def GCD( a,b ) :
    if ( b > a ) :
        a,b = b,a
    # a와 b중 큰 수를 a와 b중 작은 수로 나눈다.
    # 나누는 나머지가 0이 될 때, 나누는 수가 최대공약수가 된다.
    while True  :
        r = a % b
        if ( r == 0 ) :
            return b
        a = b
        b = r
        
# 최소공배수 = 두 수의 곱을 최대공약수로 나눈다.
def LCM( a,b ) :
    ret = (a * b) // GCD(a,b)
    return ret

def solution (a,b) :
    ret = LCM(a,b)
    return ret

a = 4
b = 6
ret = solution( a,b )
print ( ret )

# 라이브러리를 import 사용하여 최대공약수 최소공배수를 구할 수 있다.

# import math
# math.gcd(a,b)
# math.lcm(a,b)
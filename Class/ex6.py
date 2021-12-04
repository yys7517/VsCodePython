def print_10times_star() :
    print('*' * 10 )

def plus( v1, v2 ) :
    """이 함수는 v1과 v2를 더한 뒤 결과를 반환하는 함수입니다."""
    result = v1 + v2
    return result

def add_multi( n1, n2 ) :
    return n1+n2, n1 * n2

def add_print(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b) )


#print_10times_star()

# print(plus.__doc__) # doc String 값을 출력.
# hap = plus(100,200)
# print(hap)

result = add_multi( 5, 10 ) # 여러 값을 반환.
# result 자료형 = tuple ( int, int ) 
print(result)  # (15, 50) 튜플 자료형으로 반환

add_print(1,9)
hap = add_print(3,4)    # add_print 함수는 반환값이 없다. 출력문만 실행하는 함수이다.
print( hap )


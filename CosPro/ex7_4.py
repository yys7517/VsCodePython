# 정수1 : 3
# 정수2 : 5
# 3 -- 5 = 12

# 정수1 : 5
# 정수2 : 3
# 5 -- 3 = 12

def m2n_sum(m,n) :
    sum = 0
    if ( m > n ) :
        t = m
        m = n
        n = t
    for i in range( m , n+1 ) :
        sum += i
    return sum


A = int(input("정수1 : "))
B = int(input("정수2 : "))
print(str(A) + " -- " + str(B)+ " = ",m2n_sum(A,B))
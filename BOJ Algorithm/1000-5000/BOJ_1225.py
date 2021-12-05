# 121*34는
# 1*3 + 1*4 + 2*3 + 2*4 + 1*3 + 1*4
# 1 * (3+4) + 2 * (3+4) + 1 * (3+4)
# ( 3+4 ) * ( 1+2+1 )
# 두 총합의 곱으로 하면 구할 수 있다.

A,B = input().split()
A = list(A)
B = list(B)

Asum = 0
for i in A :
    Asum += int(i)

Bsum = 0
for j in B :
    Bsum += int(j)

print( Asum * Bsum )
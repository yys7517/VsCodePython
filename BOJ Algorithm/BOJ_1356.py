# 백준 브론즈 1 - 유진수
import sys

n = list(input())

length = len(n)

if( length <= 1 ) :
    print("NO")
    sys.exit()

# print(n)

# 0 1 2
for i in range( length-1 ) :
    num = 1
    num1 = 1
    for j in range( 0, i+1 ) :
        num *= int(n[j])
    for k in range( length -1, i , -1 ) :
        num1 *= int(n[k])
    if ( num == num1 ) :
        print("YES")
        sys.exit()
    
print("NO")
    
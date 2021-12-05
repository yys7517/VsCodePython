# 백준 브론즈 2 - 이진수 덧셈
'''
A, B = map(str, input().split())

# 입력받은 두 이진수를 십진수로 변환해준다.
A = int(A, 2)
B = int(B, 2)

# 십진수로 변환된 이진수를 합하여 십진수 C를 구한다.
C = A + B

# C를 다시 2진수로 변환해준다.
# 인덱스 2부터 슬라이싱하는 이유는 0b를 생략해주기 위함이다.
print(bin(C)[2:])
'''

# 10진수로 만든 후, 10진수 덧셈 후, 2진수로 다시 변환할 것.

# 밑에 쌩쇼를 하면서 풀었는데 
# 위에 처럼 풀면 되게 간단하다.

def square(a,b) :
    if ( a == 1 or b == 0 ) :
        return 1
    else :
        return a**b

A,B = input().split()
A = list(A)
B = list(B)

# A를 10진수로
DecA = 0
for i in range( len(A) ) :
    DecA += int(A[i]) * square( 2 , len(A) - (i + 1) )

# print(DecA)

# B를 10진수로
DecB = 0
for i in range( len(B) ) :
    DecB += int(B[i]) * square( 2 , len(B) - (i + 1) )

# print(DecB)

import sys
Decresult = DecA + DecB
# 합이 0이면 0 출력, 프로그램 종료.
if ( Decresult == 0 ) :
    print(0)
    sys.exit()

# 합이 0이 아니면
result = ''
while( Decresult > 0 ) : 
    share = Decresult // 2
    rest = Decresult % 2
    result = str(rest) + result 
    Decresult = share


# 리스트로 변환 후, 1 보다 앞 인덱스에 0 이 있는지 확인.
resultlist = list(result)
# print(resultlist)

# ValueError 방지 try-except문
try :
    # 0이 1보다 앞에 있으면, 1이 처음 나오는 부분부터 슬라이싱하여 출력.
    if ( resultlist.index('0') < resultlist.index('1') ) :
        print( result[resultlist.index('1') : ] )
    else :  # 1이 0보다 앞에 있어도 1부터 슬라이싱해서 출력해도 된다.
        print( result[resultlist.index('1') : ] )
except ValueError:
    print(result)       # ValueError가 났을 시에는 그냥 result값 출력.
                        # index 함수로 값을 찾지 못할 경우 ValueError 발생.
                        # resultlist.index('0') < resultlist.index('1') 
                        # 과정에서 둘 중 하나 값이 없을 때 ( 00000000000000000 or 1111111111111111 )
                        # 또는 둘의 값이 없을 때 발생할 수 있다. ( 둘의 값이 없을 수는 없다. )
                        # 00000000000000 은 위에 십진수 덧셈에서 처리하여 있을 수 없고 
                        # 11111111111111 의 경우는 그냥 result 출력하면 된다.
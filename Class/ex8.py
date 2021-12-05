# def factorial(n) :
#     result = 1

#     for i in range(1, n+1):
#         result *= i

#     return result

# print('5! = ', factorial(5))

# import math
# a = math.factorial(5)
# print('5! = ', a)

# from 모듈이름 import 함수이름
# 함수이름만을 호출해서 사용 가능

from math import factorial
from math import comb
import math
# math 모듈 내 factorial, comb 함수만 사용 가능.
# == from math import factorial,comb

# from math import *    
# math 모듈의 모든 변수,함수,클래스를 사용 가능.


# b = math.comb(5,2)
# math 모듈 내 모든 함수를 사용하려면
# import math를 해서 사용하자.

b = comb(5,2)
print('5 combination 2 = ', b)

from math import pow,sqrt

a = pow(2,3)
b = sqrt(4)

print( a )
print( b )

import math as m
# 별칭으로 사용할 수 있다.
from math import pow as p, sqrt as s

a = p(2,3)
b = s(4)
print( a )
print( b )
print(dir(math))
del math            # math 모듈 해제.

import importlib
import math
importlib.reload(math)

print(dir(math))    # math 모듈이 해제 되므로 오류. reload 시 dir로 함수,변수 목록 다시 불러올 수 있음.


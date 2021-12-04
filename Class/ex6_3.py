# 일반 함수 : 재사용을 위해 함수를 메모리에 할당
# 람다 함수 : 한 번 사용하고 메모리에서 삭제
# 여러 개의 매개변수를 가질 수 있으나 반환값은 한 개.
# lamda 키워드를 사용

def add(n,m) : 
    return n+m

# print('add함수:', add(2,5) )

# # 람다함수로 작성
# print( 'lambda함수:',(lambda n,m : n+m)(2,5) )





# filter( 함수 , 리스트 ) : 리스트에 있는 원소들을 함수에 적용하여 
# 결과가 참인 값들로 새로운 리스트를 만듬

# map( 함수 , 리스트 ) : 리스트에 있는 원소들을 함수에 적용한 후 
# 새로운 리스트에 저장하고 반환

# reduce( 함수 , 리스트 ) : 리스트에 있는 원소들을 
# 누적적으로 함수에 적용한 후 반환

product1 = 1
list1 = [1,2,3,4]
for num in list1 :
    product1 = product1 * num
print( 'product1 = ', product1 )

# reduce()를 사용하는 경우
from functools import reduce
product2 = reduce( (lambda x,y: x*y), [1,2,3,4] )
print('product2 = ', product2)

def cube(y) :
    return y * y * y

g = lambda x : x * x * x
print('print g(7) = ' ,g(7))
print('print cube(5) = ' ,cube(5))

# lambda 함수와 함께 사용한 filter() 함수
li = [5,7,22,97,54,62,77,23,73,61]
print('li = ',li)
final_list_filter = list(filter( lambda x: (x % 2 != 0) , li ))
print('print(final_list_filter) = ', final_list_filter)

# lambda 함수와 함께 사용한 map() 함수
final_list_map = list(map( lambda x: x * 2, li ))
print('print(final_list_map) = ', final_list_map)

# reduce()

li = [5,8,10,20,50,100]
sum = reduce( (lambda x,y : x+y),li )
print('print(sum) = ', sum)

product = reduce((lambda x,y: x*y),[1,2,3,4] )
print('print(product) = ',product)

string = reduce((lambda x,y: y+x),'abcde')
# ba
# cba
# dcba
# edcba
print('print(string) = ',string)

a = [1,2,3,4,5,6,7,8,9,10]
a_lambda = list(map( lambda x: str(x) if x % 2 == 0 else x , a))
print(f'a = {a}')       # fstring
print('a_lambda = ', a_lambda) 

b_lambda = list(map(lambda x:str(x) if x == 1 else float(x) if x == 2 else x+ 10,a))
print('b_lambda = ',b_lambda)

# 조건식이 여러 개 일때는 람다식 말고 그냥 함수를 사용하자

def f(x):
    if x==1 :
        return str(x)
    elif x==2 :
        return float(x)
    else :
        return x+10

c_lambda = list(map(f,a))
# a 리스트에 있는 원소들을 함소에 적용한 후, 
# 새로운 리스트에 저장하고 c_lambda에 반환.

print('c_lambda = ',c_lambda)

# map( 함수 , 리스트 ) : 리스트에 있는 원소들을 함수에 적용한 후 
# 새로운 리스트에 저장하고 반환
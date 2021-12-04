# 기본값이 없는 매개변수는 기본값이 있는 매개변수 뒤에 올 수 없다.
# 안되는 예시 : def student( name, id_no = '비공개', phone) :

def student(name, phone, id_no = '비공개' ):
    print('이름 : ', name)
    print('전화번호 : ', phone)
    print('주민번호 : ', id_no)

# 가변매개변수
# 여러개의 값을 매개변수로 입력 받을 때..
def add_m(*args) :
    result = 0
    for i in args : 
        result += i
    return result

r1 = add_m(1,2,3)
print('r1 = ', r1)

r2 = add_m(1,2,3,4)
print('r2 = ', r2)

r3 = add_m(1,2,3,4,5,6)
print('r3 = ', r3)

# 가변 매개변수는 일반 매개변수와 같이 사용이 가능하다.
# 일반 매개변수는 가변 매개변수 뒤에 사용할 수 없다.
# 가변 매개변수는 하나만 사용이 가능하다.
print()

def value_times( times, *values) :
    """가변 매개변수와 일반 매개변수를 함께 사용한 함수이다."""
    for i in values :
        print( times * i )

print(value_times.__doc__)
value_times(3,1,2,3,4,5)
# times = 3
# values = (1,2,3,4,5)
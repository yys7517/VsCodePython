# 지역변수가 전역변수보다 우선시 되어 사용
# global 키워드를 사용하여 전역 변수의 값을 변경하거나 호출할 수 있음.
# 지역변수와 전역변수가 변수명이 같을 때, global 키워드로 구분하거나, 변수명만 사용하면 지역변수를 호출

# def f_a() :
#     num = 20
#     print("f_a()의 num 값 %d" % num)

# def f_b() :
#     print("f_b()의 num 값 %d" % num)

# num = 10
# f_a()
# f_b()


def f_a() :
    global num          # num은 전역변수 num이다.
    num = 20            # 전역변수 num 값 수정.
    print("f_a()의 num 값 %d " % num)

num = 10
f_a()
print("전역변수 num값 %d"% num)
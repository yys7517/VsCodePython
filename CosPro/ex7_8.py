def calc(num1,num2,act="+") :
    if act == "+" :
        return num1+num2
    elif act == "-":
        return num1-num2
    elif act == "*" :
        return num1*num2
    elif act == "/" :
        return num1/num2
    else :
        return "잘못된 형식입니다."

num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))
act = input("연산자 : ")

if ( calc(num1,num2,act) == "잘못된 형식입니다." ) :
    print("잘못된 형식입니다.")
else :
    print("두 수의 연산결과 : ", calc(num1,num2,act))



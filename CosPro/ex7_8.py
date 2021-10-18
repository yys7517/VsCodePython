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
        return "잘못된 연산기호입니다."

num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))

print (calc(num1,num2,"+"))
print (calc(num1,num2,"*"))
print (calc(num1,num2,"^"))



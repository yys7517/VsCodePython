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


n1 = int(input("정수1 : "))
n2 = int(input("정수2 : "))

print (calc(n1,n2,"*"))
print (calc(num1=n1,num2=n2,act="*"))
print (calc(num2=n2,num1=n1,act="*"))
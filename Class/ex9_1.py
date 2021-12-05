def divide(x,y):
    try : 
        result = x / y
        # raise 예외객체명('예외내용')
        # raise 를 사용하여 직접 예외를 발생시킬 수 있다.
    except ZeroDivisionError as zero_div_err:
        print("0으로 나눌 수 없습니다.",zero_div_err)
    else :
        print("정상적으로 나눗셈이 실행되었습니다. 결과는 %d 입니다." % result)
    finally :
        print("\n프로그램을 종료합니다.")

input_a = int(input("피제수를 입력해주세요 : "))
input_b = int(input("제수를 입력해주세요 : "))
print()
divide(input_a,input_b)

try : 
    input_x = int(input('짝수를 입력하세요: '))
    if input_x % 2 != 0 :
        raise Exception('짝수가 아닙니다.')
    
    if input_x == 0 :
        raise Exception('0을 입력하셨습니다.')

except Exception as e:
    print('예외가 발생했습니다.',e)
else :
    print("입력한 수는 %d 입니다." % input_x)
finally :
    print("\n프로그램을 종료합니다.")



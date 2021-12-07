# 입력받은 number가 완전수인지 판별하는 문제.
# 완전수란 ? 자기 자신을 제외한 양의 약수들의 합이 자기자신이 되는 것.
while True :
    number = int(input())
    if number == -1 :   # -1을 입력받을 시 프로그램을 종료한다.
        break
    else :
        list1 = []
        sum = 0
        for i in range( 1, number ) :
            if number % i == 0 :
                list1.append(i)
                sum += i

        if sum == number :
            print( "%d = " % number, end='')
            for i in range( len(list1) ) :
                if i == len(list1) - 1 :
                     print("%d\n" %list1[i] ,end='')
                else:
                    print("%d + " % list1[i] ,end='')
        
        else :
            print("%d is NOT perfect." % number)

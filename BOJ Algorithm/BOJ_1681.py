N,L = map(int,input().split())

number = 1       # 양의 정수로 라벨링 1부터 시작


while True :
    list1 = list( str(number) )
    #print(list1, end =' ')
    if ( list1.count(str(L)) >= 1 ) :
        number += 1
    else:
        N -= 1
        if ( N == 0 ) :
            break
        #print( N )
        number += 1
         

print(number)
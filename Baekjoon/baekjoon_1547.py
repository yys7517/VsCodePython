# 백준 브론즈3 - 공

# 공이 초기에는 1번 컵에 있다.
# balllist = [True,False,False]
list = [1,2,3]

M = int(input())
for i in range(M) :
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    # 인덱스 값을 기준으로 하기 위해 값을 1씩 뺀다.
    # 리스트의 인덱스를 통해 방문할 것이다.
    xi = list.index(X)
    yi = list.index(Y)

    list[xi],list[yi] = list[yi],list[xi]
    # X = int(X) - 1  
    # Y = int(Y) - 1 
    # if ( balllist[X] == True ) :
    #     if ( balllist[Y] == False ) :
    #         balllist[X] = False
    #         balllist[Y] = True
    # else :
    #     if ( balllist[Y] == True ) :
    #         balllist[X] = True
    #         balllist[Y] = False
    #     else :
    #         continue

# print( balllist.index(True) + 1 ) 
print( list[0] )
# 백준 브론즈 3 - 주사위 게임.
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
N = int(input())
moneylist = []
for i in range(N) :
    X,Y,Z = map ( int, input().split() )
    if ( X == Y and Y == Z ) :
        moneylist.append( 10000 + X * 1000 ) 
    elif ( X == Y ) :
        moneylist.append( 1000 + X * 100 ) 
    elif ( Y == Z ) :
        moneylist.append( 1000 + Y * 100 ) 
    elif ( X == Z ) :
        moneylist.append( 1000 + X * 100 ) 
    else :
        moneylist.append( max( X , max( Y, Z) ) * 100 ) 

print( max(moneylist) )

# 백준 브론즈 3 - 카드 놀이
# 만약, A와 B의 총 승점이 같은 경우에는, 제일 마지막에 이긴 사람을 게임의 승자로 정한다. 
# 그래도 승부가 나지 않는 경우는 모든 라운드에서 비기는 경우뿐이고 이 경우에 두 사람은 비겼다고 한다.
ACards = []
BCards = []

AScore = 0
BScore = 0

ACards = input().split()
BCards = input().split()

winner = ""
for i in range( 10 ) :
    if ( int(ACards[i]) > int(BCards[i]) ) :
        AScore += 3
        winner = "A"
        
    elif ( int(ACards[i]) < int(BCards[i]) ) :
        BScore += 3
        winner = "B"
    else :
        AScore += 1
        BScore += 1

print( AScore, end=' ')
print( BScore )

if( AScore > BScore ) :
    print('A')
elif( AScore < BScore ) :
    print('B')
elif ( AScore == BScore ) :
    if ( winner == "A" ) :
        print("A")
    elif ( winner == "B" ) :
        print("B")
    else :
        print("D") 



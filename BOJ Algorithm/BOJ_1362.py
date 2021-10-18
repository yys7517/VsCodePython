# 백준 브론즈 2 - 펫
# 적정 체중 o, 실제 체중 w 를 입력하면서 시나리오가 시작.
# "# 0 "을 입력하면 한 시나리오 종료.
# 0 0을 입력하면 모든 시나리오 끝.
# 실제 체중이 적정 체중의 1/2배를 초과하면서 적정 체중의 2배 미만이라면 펫은 행복합니다. 
# 펫의 실제 체중이 0 이하일 경우 펫은 사망하게 되며, 
# 그 외의 경우 펫은 슬픕니다.


Scenario = 1
pet = {}

while True :
    o,w = map (int, input().split())
    die = False
    if ( o == 0 and w == 0 ) : 
        Scenario -= 1
        break

    while True:
        Action, value = input().split()
        if ( Action == '#' and value == '0' ) :
            break

        # Action == F , 먹이 주기
        # Action == E , 운동 시키기
        if not die :             # 죽지 않았을 때만 처리.
            if ( Action == 'F') :
                w += int(value)
            elif ( Action == 'E') :
                w -= int(value)

        if ( w <= 0 ) :         # 죽었으면 아무런 처리도 하지않고 # 0 을 기다린다.
            die = True

    if ( w <= 0 ) :                      # 사망
        pet.update( { Scenario : "RIP"} )  
        Scenario += 1
        continue  
    elif ( w > o / 2 and w < o * 2 ) :    # 행복
        pet.update( { Scenario : ":-)"} )
        Scenario += 1
        continue
    else :                                 # 슬픔
        pet.update( { Scenario : ":-("} )
        Scenario += 1
        continue
    
    

for i in range( 1, Scenario + 1 ) :
    print( i, end=' ')
    print( pet.get(i) )


def solution( people ):
    # [S, M, L, XL] 순으로 리스트에 담아 return 합니다
    counter = [ 0 for i in range(4) ]
    for i in people : 
        if ( i < 95 ) :
            counter[0] += 1
        elif( i >= 95 and i < 100 ) :
            counter[1] += 1
        elif( i >= 100 and i < 105 ) :
            counter[2] += 1
        else : 
            counter[3] += 1

    return counter

# 덩치              사이즈
# 95 미만             S
# 95 이상 100 미만    M  
# 100 이상 105 미만   L 
# 105 이상            XL  



# 주문해야 하는 유니폼 사이즈의 수를 순서대로 담은 리스트를 출력

people = [97, 102, 93, 100, 107] 
ret = solution( people )
print( ret )
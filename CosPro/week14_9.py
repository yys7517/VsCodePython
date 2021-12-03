def solution( taekwondo, running, shooting ) :
    ret = 0
    if ( taekwondo >= 25 ) :
        ret += 250
    else :
        ret += 8 * taekwondo
    
    runbenefit = 60 - running
    if ( runbenefit == 60 ) :
        ret += 250
    else : 
        ret += 250 + runbenefit * 5
    
    count = 0   # 10 과녁 맞춘 개수
    for i in shooting : 
        if i == 10 :
            count += 1
        ret += i
    
    if count >= 7 :
        ret += 100

    return ret


taekwondo = 27
running = 63
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
ret = solution ( taekwondo,running,shooting)
print( ret )
def solution( speed, cars ) :
    ret = 0
    for i in cars :
        if ( i >= int (1.1 * speed) and i < int(1.2 * speed) ) :
            ret += 3
        elif ( i >= int(1.2 * speed) and i < int(1.3 * speed) ):
            ret += 5
        elif ( i >= int(1.3 * speed) ) :
            ret += 7
        
    return ret

cars = [110, 98, 125, 148, 120, 112, 89] 
speed = 100
ret = solution( speed, cars )
print( ret )
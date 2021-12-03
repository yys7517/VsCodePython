def solution( point ) :
    if ( point >= 1000 ) :
        return ( point // 100 ) * 100


point = 2323
ret = solution( point )
print ( ret )
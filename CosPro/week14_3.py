def solution( n, votes ):
    counter = [ 0 for i in range(n) ]
    for i in votes :
        counter[ i-1 ] += 1
    # print( counter )
    count = 0
    for i in counter : 
        if ( i == max(counter) ) :
            count += 1

    # counter 의 인덱스 값이 후보 번호이다.
    for i in range( len(counter) ) :
        if( counter[i] == max(counter) and count == 1 ) :
            result = i+1
        elif( count > 1) :
            result = -1

    return result

n = 2
votes = [2,1,2,1,2,2,1,1]
ret = solution( n, votes )
print( ret )
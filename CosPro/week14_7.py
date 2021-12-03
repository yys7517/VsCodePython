def solution(time_table) :
    firstidx = time_table.index(1)
    lastidx = 0
    count = 0

    for i in range(len(time_table)) :
        if ( time_table[i] == 1 ) :
            lastidx = i

    for i in range(firstidx, lastidx):
        if( time_table[i] == 0 ) :
            count += 1
            
    return count

time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]


ret = solution(time_table)
print( ret )
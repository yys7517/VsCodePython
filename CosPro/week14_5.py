def solution( scores, cutline ) :
    count = 0
    for i in scores :
        if ( i >= cutline ) :
            count += 1

    return count


scores = [80, 90, 55, 60, 59]
cutline = 60

ret = solution( scores, cutline )
print ( ret )
def solution(number) :
    numtolist = list(str(number))
    count = 0
    print( numtolist )
    for i in numtolist :
        if ( i == '2' or i == "3" or i == '5' or i =='7' ) :
            count += 1


    return count




number = 29022531
print ( solution(number) )
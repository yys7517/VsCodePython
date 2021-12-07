def solution( order, list1 ) :
    ordertolist = list(order)
    for i in ordertolist :
        if i == "A" :
            tmp = list1[0]
            list1[0] = list1[1]
            list1[1] = tmp
        elif i == "B" :
            tmp = list1[1]
            list1[1] = list1[2]
            list1[2] = tmp
        else : 
            tmp = list1[0]
            list1[0] = list1[2]
            list1[2] = tmp

    for i in range(0, len(list1) ) :
        if list1[i] == 1 :
            return i+1

order = input()
list1 = [ 1,0,0 ]
ret = solution(order,list1)
# 값이 1인곳이 공이 있는 위치.
print( ret )

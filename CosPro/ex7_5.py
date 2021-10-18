def pzn(n) :
    if ( n > 0 ) :
        return 1
    elif ( n == 0 ) :
        return 0
    else :
        return -1

while True : 
    N = int( input("정수 : ") )
    if ( pzn(N) == -1 ) :
        print('음수')
    elif ( pzn(N) == 0 ) :
        print(0)
        break
    else :
        print("양수") 
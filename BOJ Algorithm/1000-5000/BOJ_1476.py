def solution( input_E, input_S, input_M ) :
    E,S,M = 1,1,1
    year = 1
    
    while True :
        if( E == input_E and S == input_S and M == input_M ) :
            break
        year += 1
        E += 1
        S += 1
        M += 1
        if E > 15 : 
            E = E % 15
        if S > 28 : 
            S = S % 28
        if M > 19 : 
            M = M % 19
        
    return year

input_E,input_S,input_M = map( int, input().split() )

year = solution( input_E, input_S, input_M )
print(year)

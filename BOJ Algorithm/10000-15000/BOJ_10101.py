# 백준 브론즈4 - 삼각형 외우기.


ang1 = int(input())
ang2 = int(input())
ang3 = int(input())

sum = ang1 + ang2 + ang3
if ( sum != 180 ) :
    print("Error")

elif ( ang1 == 60 and ang2 == 60 and ang3 == 60) :
    print("Equilateral")

elif ( sum == 180 ) : 
    if ( ang1 == ang2 or ang2 == ang3 or ang1 == ang3 ) : 
        print("Isosceles")
    else :
        print("Scalene")


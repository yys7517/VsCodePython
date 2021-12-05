# 백준 브론즈 2 - 책 정리

N, M = map(int,input().split())
Box = list( map (int,input().split()) )
Book = list ( map (int,input().split()) )

# print(Box)
# print(Book)

for i in range(len(Box)) :
    for j in range(len(Book)) :
        if Box[i] >= Book[j] :
            Box[i] -= Book[j]
            Book[j] = 0
            if ( Box[i] == 0 ) : 
                break
        
# print(Box)
# print(Book)

print( sum(Box) )
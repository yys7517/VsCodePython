n = int(input())

Trophys = []
for i in range(n) :
    x = int(input())
    Trophys.append(x)

# print(Trophys)

left = 1
right = 1

# left
for i in range(0 , n-1) :
    if  Trophys[i] >= Trophys[i+1] :
        break
    else :
        left += 1


# right
for i in range( n-1, 0, -1 ) :
    if  Trophys[i] >= Trophys[i-1] :
        break
    else :
        right += 1


print(left)
print(right)
n = int(input())

Trophys = []
for i in range(n) :
    x = int(input())
    Trophys.append(x)

# print(Trophys)

left = 0
right = 0
h = 0

# left
for i in range(0 , n) :
    if  h < Trophys[i] :
        h = Trophys[i]
        left += 1


h = 0
# right
for i in range( n-1, -1, -1 ) :
    if  h < Trophys[i] :
        h = Trophys[i]
        right += 1


print(left)
print(right)
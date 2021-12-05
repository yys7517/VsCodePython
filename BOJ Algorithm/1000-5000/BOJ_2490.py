# 백준 브론즈 3 - 윷놀이.
# 배 - 납작한 부분 , 등 - 볼록한 부분
# 배(0), 등(1)

# 걸 - 배 3개, 등 1개
# 도 - 배 1개, 등 3개
# 도개걸윷모 - ABCDE

list = []

for i in range(3) :
    sublist = input().split()
    list.append(sublist)

# print(list)

for i in list :
    if ( i.count('0') == 0 ) :
        print("E")
    elif( i.count('0') == 1 ) :
        print("A")
    elif( i.count('0') == 2 ) :
        print("B")
    elif( i.count('0') == 3 ) :
        print("C")
    elif( i.count('0') == 4 ) :
        print("D")
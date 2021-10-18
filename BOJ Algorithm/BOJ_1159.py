# 백준 브론즈 2 - 농구 경기
N = int(input())
firstnamelist = []
# 입력받은 선수들의 초성을 중복 허용하여 모두 넣는다.
# ex ) b - 7개, h - 1개 ........

for i in range(N) :
    name = input()
    firstnamelist.append( name[0:1] )
# 입력받은 선수들의 초성을 중복 허용하여 모두 넣는다.
# ex ) b - 7개, h - 1개 ........
    

firstnameset = set(firstnamelist)       # 초성의 중복을 제거하기 위해 set으로 변환해준다. set에는 중복값을 제거한 초성들이 들어가있다.
uniquefnamelist = list(firstnameset)    # 이 set의 값을 가져와서 비교하기 위해 다시 list로 변환해준다. 중복된 값이 제거된 list가 된다.

firstnamelist.sort()
uniquefnamelist.sort()
result = ""                             

for i in uniquefnamelist :                  # i 값은 초성이 된다.
    if ( firstnamelist.count(i) >= 5 ) :    # 초성의 개수가 5 이상일 때, 그 초성을 가진 선수들을 명단에 포함시킨다.
        result += i

if ( result == ""  ) :
    print("PREDAJA")
else :
    print(result)
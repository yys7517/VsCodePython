# 백준 브론즈 2 - 노래 악보
N,Q = map (int,input().split())
# N 개의 악보


Blist = []
for i in range (N) :
    B = int(input())
    Blist.append(B)
# Blist 에는 악보가 차지하는 시간을 넣는다.
# [2,1,3] = 1번 악보 2초, 2번 악보 1초, 3번 악보 3초 를 뜻한다.\
Time = []

num = 1 # 악보번호

for i in Blist :
    for j in range(i) :
        Time.append( num )
    num += 1
    
# print(Time)


result = []
# Q는 Q초에 무슨 악보를 부르는지 물어보는 질문이다.
for i in range (Q) :
    t = int(input())
    result.append (Time[t])

for i in result : 
    print(i)
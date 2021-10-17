# 백준 브론즈 3 - 지능형 기차 1.

N = 4
# 4개의 기차역

max = 0
sum = 0
for i in range(N) :
    # 내리는 사람 수 X, 타는 사람 수 Y
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    sum += Y - X
    if ( sum > max ) : 
        max = sum
print(max)
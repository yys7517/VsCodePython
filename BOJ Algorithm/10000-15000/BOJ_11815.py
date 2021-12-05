count = int(input()) 
num = list(map(int, input().split())) 

# print(num)

# 제곱수의 특징 4, 9, 16, 25 ......
# 제곱수들은 항상 약수가 홀수개이다.
# 수를 루트를 씌웠을 때 그 값이 정수값으로 떨어지면 그 수는 제곱수이다.
# 따라서 그 제곱근을 다시 제곱했을 때, 처음과 같은 값이 된다면 제곱수이다.

for i in range(count): 
    if num[i] == (int(num[i] ** 0.5) ** 2):     # 제곱수이냐 ? 
        print(1, end = " ") 
    else: 
        print(0, end = " ")


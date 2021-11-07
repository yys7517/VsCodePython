'''
def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:    
                # 1의 자리가 3 6 9
                count += 1
                print("clap", end = '')
            current = current // 10 
            # 30, 31, 32, 34, 35, 37, 38, 61, 62, 64, 65... 의 경우
            # current를 10의 자리 수를 구해서 10의 자리가 3 6 9 일 때도, clap
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count
'''

def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = list(str(i))     # 현재 숫자
        for j in current :
            if ( j == '3' or j == '6' or j =='9' ) :
                count += 1
        
    return count

number = 40
ret = solution(number)

print("Solution: return value of the function is", ret, ".")

# 369 게임..
# 1부터 number의 수 까지 369 게임을 진행할 때 손뼉을 치는 횟수를 구하라.
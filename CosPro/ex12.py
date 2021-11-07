def func_a(arr):
    counter = [0 for _ in range(1001)]      # 1001 길이의 리스트를 선언.
    for x in arr:
        counter[x] += 1                     # 값이 x이면 x번째 값 + 1 ==  x의 개수 + 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:             # x의 값이 더 크면.
            ret = x             # x의 값을 ret에 넣는다..
    return ret                  # 최대값을 구하는 함수.

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:  # x의 값이 더 작으면..
            ret = x             # x의 값을 ret에 넣는다..
    return ret                  # 최소값을 구하는 함수.

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt


arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)


print("Solution: return value of the function is", ret, ".")

# 리스트 내의 자연수의 개수를 센다.
# 가장 많은 자연수의 개수가 가장 적은 자연수의 개수의 몇 배 이상 많은가 ? 

##### 매개변수 설명
# 자연수가 들어있는 리스트 arr가 solution 함수의 매개변수로 주어집니다.
# arr의 길이는 3 이상 1,000 이하입니다.
# arr에는 1 이상 1,000이하의 자연수가 들어있습니다.
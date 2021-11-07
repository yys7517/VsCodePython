def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # month의 총 일 수
    # 1월 : 31일, 2월 : 28일, 3월 : 31일....................
    # 윤년 고려 X
    total = 0
    for i in range(month - 1):      # ex ) month = 2이면, 1월 1일과는 31일 + day만큼의 차이.
        total += month_list[i]
    total += day
    return total - 1            # 1월 1일부터 그 month, day까지 날짜이므로 총 날짜합에 
                                # 마지막에 1을 빼준다.
        
def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total
        
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

print("Solution: return value of the function is", ret, ".")


# 두 날짜 사이의 일 수를 구하는 문제이다.
# 두 날짜 사이의 일 수는 1월 1일부터 두 날짜 간 차이나는 일 수를 구한 다음
# 서로의 차를 구하면 된다.
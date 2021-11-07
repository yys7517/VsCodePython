
def solution(price, grade):
    sales = { "S" : 0.05, "G" : 0.1, "V":0.15 }
    answer = int ( price - ( price * sales.get(grade) ) )

    
    return answer

price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)


print("Solution: return value of the function is", ret1, ".")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

print("Solution: return value of the function is", ret2, ".")

# 등급에 따른 할인율이 적용된 금액을 반환하라.
# "S"   5%
# "G"   10%
# "V"   15%
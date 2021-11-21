def solution( purchase ) :
    result = 0  # 상품권 금액
    for i in purchase :
        if ( i >= 1000000 ) :
            result += 50000
        elif ( i >= 600000 ) :
            result += 30000
        elif ( i >= 400000 ) :
            result += 20000
        elif ( i >= 200000 ) :
            result += 10000
    return result

purchase = [150000, 210000, 399990, 990000, 1000000]

print ( solution(purchase) )
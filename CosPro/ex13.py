'''
def solution(arr):
    left, right = 0, len(arr)-1
    # 양 끝을 바꿔주고.
    # 전체가 바뀔 때까지..
    # 리스트의 길이가 4일 때 2번 반복..
    # 리스트의 길이가 5일 때도 2번 반복.. 가운데 수는 그대로 둔다.
    # 리스트의 길이가 6일 때 3번 반복..
    # 리스트의 길이 // 2 만큼 반복한다.
    i = 0
    while i < len(arr) // 2:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        # left를 1증가, right를 1감소 시켜서 바꿔주고..
        i += 1          # len(arr) // 2 의 횟수 만큼 반복하기 위한 i 값 + 1
                        # 리스트의 길이가 4이면 len(arr) // 2의 값은 2..
                        # i = 0, i = 1 일때 반복.
    return arr
'''
def solution(arr):
    left, right = 0, len(arr)-1
    # left의 값이 right보다 작을 때만 반복해도 되더라...
    # 기억하자..
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr


arr = [1, 4, 2, 3]
ret = solution(arr)


print("Solution: return value of the function is ", ret, " .")


# 주어진 리스트의 순서를 뒤집는 문제.
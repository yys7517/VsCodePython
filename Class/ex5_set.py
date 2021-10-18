set1 = {1,2,3,4,2,3,4,5,3,4,5,6,7,7,7,7,7}
print (set1)
list1 = ['국어','영어','수학','영어','국어']
print(list1)
# 리스트 set로 변경
print(set(list1))
# 집합 set은 인덱스로 접근할 수 없다.
print(set1[0])

# add
set1.add(8)

# update
set1.update([9,10])

# remove
#set1.remove(7)
#set1.remove(7) # 값이 없으면 오류 발생

# discard
# 값이 없더라도 오류가 발생하지 X
set1.discard(7)
set1.discard(7)

set1 = set('python world')
print(set1)

set1 = set(range(10))

set1 = {0,1,2,3,4,5}
set2 = {4,5,7,8,2,1}
print("set1 | set2 = ", set1 | set2)
print("set1 & set2 = ", set1 & set2)

print("set1 - set2 = ", set1 - set2)
print("set2 - set1 = ", set2 - set1)

print("set1 ^ set2 = ", set1 ^ set2 )
print( set1.symmetric_difference )

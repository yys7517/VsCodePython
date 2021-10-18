# 딕셔너리 (dictionary)
# key 와 값 { 키1:값1, 키2:값2 ...... }
# key 는 유일하다. 인덱스로 접근 불가, key 로만 접근
# 튜플은 키로 사용가능, 리스트로는 키로 사용 불가
# 리스트는 변경 가능하기 때문에.

# 빈 딕셔너리
# dic1 = {}
# print( dic1 )
# dic2 = dict()
# print( dic2 )

dic1 = { 'name' : '홍길동', 'phone' :  '010-3224-8732', 'birth' : '03-01'}
# print(dic1)
# dic2 = { '점수' : [99,85,90] }
# print(dic2)

# 삽입 및 수정.

# # 딕셔너리이름[ key ] = 값

# # 없는 키 값이라면 키와 값을 추가.
# dic1['major'] = '컴퓨터공학'
# print(dic1)

# # 키 값이 있는 값이라면 키에 따른 값 수정.
# dic1['birth'] = '05/01'
# print(dic1)

# 값 조회
# print( 딕셔너리이름[ key ] )
 
# print( dic1['name'] )

# 값 삭제 ( del )

# del ( 딕셔너리이름[ key ] )

# del ( dic1['phone'] )
# print ( dic1 )
# del ( dic1['name'] )
# print( dic1 )

# 값 반환 후 삭제 ( pop )
# pop( key )

# popitem
# 딕셔너리의 마지막 키-값 쌍을 반환 후 삭제.
# print ( dic1.popitem() )
# print(dic1)

# print ( dic1.popitem() )
# print(dic1)

# keys
# 딕셔너리의 key만을 모아서 반환.
# print( dic1.keys() )

# values
# 딕셔너리의 value만을 모아서 반환
# print( dic1.values() )

# items
# 딕셔너리의 key-value 쌍을 튜플로 묶은 값을 반환
# print( dic1.items() )

# len
# print( len(dic1) )

#clear
# dic1.clear()
# print(dic1)

# get
# dic1.get(key)
# key 따른 value값을 반환.
# key가 존재하지 않으면 keyError 발생.

# update ( 수정 )
# key값이 있으면 그 값 수정
# key값이 없으면 key-값 쌍 추가

# print('# update #')
# print( dic1 )
# print()

# dic1.update( {'name' : '윤영선', 'birth':'10/01','grade':'1','address':'seoul'})
# print( dic1 )
# print()

# dic1.update( name = "김영희", birth = "12/25", grade= "4")
# print ( dic1 )
# print()

from pprint import pprint as pp
pp (dic1)
import sys

s = sys.stdin.read()
cnt = [0]*26
# 26 길이의 리스트 ( 알파벳 개수 리스트 ) 그래서 0 으로 초기화.

# 알파벳 소문자 a를 리스트의 첫 번째에 넣으려면.
# a가 0번째니까 찾은 알파벳 s 값에서 a의 아스키 코드값을 빼주면
# # 알파벳 s의 인덱스 값을 구할 수 있다.
for c in s:
    if c.islower():
        cnt[ ord(c)-ord('a') ] += 1

result =''
for i in range( len(cnt) ):
    if cnt[i] == max(cnt):
        result += chr( i + ord('a') )

print(result)
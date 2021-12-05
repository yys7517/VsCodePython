# 백준 브론즈 2 - 모음의 개수
# 주어진 문장의
# 모음의 개수 a,e,i,o,u 의 개수를 세자.
Search = [ 'a','e','i','o','u','A','E','I','O','U' ] 

while True :
    count = 0
    Sentence = list(input())
    if ( '#' in Sentence ) :
        break
    else :
        for i in Sentence :
            if ( i in Search ) :
                count += 1

        print(count)
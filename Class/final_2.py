import random as r
rsp_list = ["가위","바위","보"]     # 가위 바위 보 리스트.

user_wincount = 0       # 사용자가 이긴 횟수
comp_wincount = 0       # 컴퓨터가 이긴 횟수

while user_wincount < 3 and comp_wincount < 3 :
    
    input_user = input("가위, 바위, 보 중 하나를 입력하시오: ")
    
    if input_user == "가위" or input_user == "바위" or input_user == "보" :
        comp_random = r.randint(0,2)            # 랜덤하게 가위 바위 보 리스트의 인덱스 값인 0 ~ 2 값 발생.
        comp_choice = rsp_list[comp_random]     # 랜덤한 인덱스 번호 값으로 컴퓨터는 가위 바위 보 3개 중 랜덤한 선택을 하게 된다.

        # 가위, 가위
        # 바위, 바위
        # 보, 보
        if input_user == comp_choice :
            print("컴퓨터 : ", comp_choice)
            print("비겼습니다")
            
        elif input_user == "가위" :
            print("컴퓨터 : ", comp_choice)
            if comp_choice == "바위" :
                print("컴퓨터 승")
                comp_wincount += 1
            else :
                print("사용자 승")
                user_wincount += 1

        elif input_user == "바위" :
            print("컴퓨터 : ", comp_choice)
            if comp_choice == "보" :
                print("컴퓨터 승")
                comp_wincount += 1
            else :
                print("사용자 승")
                user_wincount += 1

        elif input_user == "보" :
            print("컴퓨터 : ", comp_choice)
            if comp_choice == "가위" :
                print("컴퓨터 승")
                comp_wincount += 1
            else :
                print("사용자 승")
                user_wincount += 1

    else : 
        print("입력오류")
        continue

print()

if user_wincount == 3 and comp_wincount < 3 :
    print("사용자 승!!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
elif user_wincount < 3 and comp_wincount == 3 :
    print("컴퓨터 승!!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
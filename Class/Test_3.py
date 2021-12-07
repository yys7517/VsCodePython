import random as r
computer = ["가위","바위","보"]

user_wincount = 0       # 사용자가 이긴 횟수
comp_wincount = 0       # 컴퓨터가 이긴 횟수

while user_wincount < 3 and comp_wincount < 3 :
    
    input_user = input("가위,바위,보 중 하나 입력 : ")
    
    if input_user == "가위" or input_user == "바위" or input_user == "보" :
        comp_random = r.randint(0,2)
        comp_choice = computer[comp_random]

        # 가위, 가위
        # 바위, 바위
        # 보, 보
        if input_user == comp_choice :
            print("사용자 : ", input_user)
            print("컴퓨터 : ", comp_choice)
            print("무승부")
            

        elif input_user == "가위" :
            if comp_choice == "바위" :
                print("사용자 : ", input_user)
                print("컴퓨터 : ", comp_choice)
                print("승자 : 컴퓨터")
                comp_wincount += 1
            else :
                print("사용자 : ", input_user)
                print("컴퓨터 : ", comp_choice)
                print("승자 : 사용자")
                user_wincount += 1

        elif input_user == "바위" :
            if comp_choice == "보" :
                print("사용자 : ", input_user)
                print("컴퓨터 : ", comp_choice)
                print("승자 : 컴퓨터")
                comp_wincount += 1
            else :
                print("사용자 : ", input_user)
                print("컴퓨터 : ", comp_choice)
                print("승자 : 사용자")
                user_wincount += 1

        else :
            if comp_choice == "가위" :
                print("사용자 : ", input_user)
                print("컴퓨터 : ", comp_choice)
                print("승자 : 컴퓨터")
                comp_wincount += 1
            else :
                print("사용자 : ", input_user)
                print("컴퓨터 : ", comp_choice)
                print("승자 : 사용자")
                user_wincount += 1

        print('-' * 50 )
        print("사용자 (%d) : 컴퓨터 (%d)" % (user_wincount, comp_wincount))
        print('-' * 50 )
        
    else : 
        print("입력오류")
        continue


if user_wincount == 3 and comp_wincount < 3 :
    print("최종 승리자 : 사용자")
elif user_wincount < 3 and comp_wincount == 3 :
    print("최종 승리자 : 컴퓨터")
def check(password, passcheck) :
    length = len(password)
    passtolist = list(password)
    capitalcount = 0
    for i in passtolist :
        if i.isupper() :
            capitalcount += 1

    if length >= 10 and capitalcount > 0 :
        if password == passcheck :
            print("유효한 비밀번호입니다~~~")
            return True
        else :
            print("비밀번호와 비밀번호 확인이 서로 다릅니다! 다시 입력해주세요!")
            return False
    else :
        print("비밀번호가 잘못되었습니다! 다시 입력해 주세요")
        return False

validcheck = False

while True :
    password = input("비밀번호 : ")
    passcheck = input("비밀번호 확인 :")
    if check( password, passcheck ) : 
        break
    
    
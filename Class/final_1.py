from datetime import datetime, timedelta

while True:
    city = int(input('도시(0.종료, 1.샌프란시스코, 2.런던, 3.시드니, 4.자카르타 ) 번호 선택 >> '))
    koreanow = datetime.now()                        # 한국의 현재 시간을 가져온다.
    koreadt = koreanow.strftime('%Y/%m/%d %H:%M')   # 연 월 일 시 분 까지만 포매팅한다.
    

    if city == 0 :                          # 0을 입력받을 시 종료.
        print('프로그램을 종료합니다.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        break

    elif city == 1 :                        # 1을 입력받을 시 한국과 샌프란시스코의 날짜 시간 출력.
        citynow = koreanow - timedelta(hours=17) # 샌프란시스코는 한국 시간 -17
        citydt = citynow.strftime('%Y/%m/%d %H:%M')
        print('한국의 현재 날짜와 시간 : ', koreadt)
        print('샌프란시스코 현재 날짜와 시간 : ', citydt)

    elif city == 2 :                        # 1을 입력받을 시 한국과 런던의 날짜 시간 출력.
        citynow = koreanow - timedelta(hours=9)  # 런던은 한국 시간 -9
        citydt = citynow.strftime('%Y/%m/%d %H:%M')
        print('한국의 현재 날짜와 시간 : ', koreadt)
        print('런던 현재 날짜와 시간 : ', citydt)

    elif city == 3 :                        # 3을 입력받을 시 한국과 시드니의 날짜 시간 출력.
        citynow = koreanow + timedelta(hours=2)  # 시드니는 한국 시간 +2
        citydt = citynow.strftime('%Y/%m/%d %H:%M')
        print('한국의 현재 날짜와 시간 : ', koreadt)
        print('시드니 현재 날짜와 시간 : ', citydt)

    elif city == 4 :                        # 4를 입력받을 시 한국과 자카르타의 날짜 시간 출력.
        citynow = koreanow - timedelta(hours=2)  # 자카르타는 한국 시간 -2
        citydt = citynow.strftime('%Y/%m/%d %H:%M')
        print('한국의 현재 날짜와 시간 : ', koreadt)
        print('자카르타 현재 날짜와 시간 : ', citydt)
    
    print()     # 한 줄 띄어쓰기

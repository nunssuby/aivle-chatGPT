import streamlit as st
import requests
import os
import openai

st.title('chatGPT API활용')
x = st.text_input("위도(x)를 넣으세요")
y = st.text_input("경도(x)를 넣으세요")


def get_sky_status(data):
    item_list = data['response']['body']['items']['item']
    for item in item_list:
        if item['fcstTime'] == '1200' and item['category'] == 'SKY' :
            selected_item = item
            break
    return selected_item['fcstValue']

# get_sky_status(data)

# 하늘 상태와 get_sky_status 함수를 이용하여 하늘 상태를 한글로 표현
def get_sky_status_kor(data):
    sky_status = get_sky_status(data)
    if sky_status == '1':
        return '맑음'
    elif sky_status == '3':
        return '구름많음'
    elif sky_status == '4':
        return '흐림'
    else:
        return '알 수 없음'

#버튼을 만들고 버튼을 누르면 아래의 코드가 실행된다.
if st.button('날씨를 확인'):
    
    #API를 호출한다.
    # url = 'http://localhost:5000/predict?x={}&y={}'.format(x,y)
    url=f"https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey=0k8h8kWmk0yI8FSQrbbh3gUNvgMzMjfKNAXR9iI%2FVOcaNDXJ5NwQOZTGo6S5dyZpQQ9ci%2BMQgAk2%2B1ygNybZfQ%3D%3D&pageNo=1&numOfRows=1000&dataType=JSON&base_date=20230407&base_time=0630&nx=55&ny=127"
    response = requests.get(url)
    data = response.json()
    weather =get_sky_status_kor(data)

    content = f'오늘 점심 날씨 {weather}. 점심 메뉴 3 가지만 추천해줘'
    #weather 을 화면에 출력한다.
    st.write(f'{content}')
    #chatGPT에게 위 내용을 요청하는 버튼 생성
    if st.button('클릭하여 chatGPT에게 위 내용을 요청'):
        #chatGPT에게 요청
        #인증 후
        print("1")
        openai.api_key = "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"
        print("2")
        #요청
        content = f'오늘 점심 날씨 {weather}. 점심 메뉴 3 가지만 추천해줘'
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}]
        )
        print(completion)
        #chatGPT의 응답을 화면에 출력
        st.write(f'chatGPT의 응답: {completion.choices[0].message.content}')
    

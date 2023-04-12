import streamlit as st
import requests
import os
import openai
import datetime

# tab1, tab2, tab3 = st.tabs(["오늘점심뭐먹을까?", "어디로여행갈까?", "오늘의주가는?"])
tab1, tab2, tab3, tab4 = st.tabs(["streamlit꾸미기", "chatGPT연동하기(API)", "내가원하는API연동하기 [공공데이터API]","비즈니스 창출 [오늘점심뭐먹을까?]"])

with tab1:
    '''
    streamlit꾸미기
    title, text_input, button 등을 배치하고 
    button 클릭 이벤트도 처리해본다
    아래 링크를 참고한다
    https://docs.streamlit.io/library/api-reference 
    '''
    #제목
    st.title('streamlit꾸미기')
    # input 입력
    input_text = st.text_input("아무 내용을 넣어보세요")
    # button
    if st.button('button을 누르시면 넣으신 내용이 나타납니다.'):
        st.write(input_text)

with tab2:
    '''
    chatGPT API를 연동해본다.
    확인을 위해 사용자로 부터 text를 입력받아서 
    chatGPT API를 통해 응답을 받고
    응답을 화면에 출력한다.
    '''
    #제목
    st.title('chatGPT연동하기(API)')
    
    # 채팅을 위한 text를 입력 받는다.
    contet = st.text_input("chatGPT에게 요청할 내용을 입력하세요")
    #chatGPT를 연동해본다.
    if st.button(label ='클릭하여 chatGPT에게 위 내용을 요청',key='chatGPTButtonTest'):
            # print("chatGPTButton button content: ", st.session_state['content'])
            #chatGPT에게 요청
            #인증 후
            openai.api_key = "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"
            #요청
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": contet}]
            )
            print(completion)
            #chatGPT의 응답을 화면에 출력
            st.write(f'chatGPT의 응답: {completion.choices[0].message.content}')  
with tab3:
    '''
    기본 chatGPT 외에 다른 API를 연동해본다.
    공공데이터를 사용해도 되고, chatGPT의 채팅 외 다른 API를 사용해도 된다.
    본인이 개발할 비즈니스에 맞춰서 추가해본다.
    '''
    st.title('내가원하는API연동하기 [공공데이터API]')
    st.header('공공데이터 날씨API 연동')
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
        
    base_date = datetime.datetime.now().strftime('%Y%m%d')

    url=f"https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey=0k8h8kWmk0yI8FSQrbbh3gUNvgMzMjfKNAXR9iI%2FVOcaNDXJ5NwQOZTGo6S5dyZpQQ9ci%2BMQgAk2%2B1ygNybZfQ%3D%3D&pageNo=1&numOfRows=1000&dataType=JSON&base_date={base_date}&base_time=0630&nx=55&ny=127"
    response = requests.get(url)
    data = response.json()
    weather =get_sky_status_kor(data)    
    st.write(f'오늘의 날씨는 {weather}입니다.')
with tab4:
    '''
    tab1 ~tab3 까지 준비된 자원들을 가지고 새로운 비즈니스를 창출한다.
    아래는 예시로 제공된다.
    '''
    st.title('비즈니스 창출 [오늘점심뭐먹을까?]')
    x = st.text_input(label="위도(x)를 넣으세요", key='x')
    y = st.text_input(label="경도(x)를 넣으세요", key='y')


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


    # content는 session_state를 통해 초기화 후 공유한다.
    content = ''
    if 'content' not in st.session_state:
        st.session_state['content'] = ''

    #버튼을 만들고 버튼을 누르면 아래의 코드가 실행된다.
    #weather 버튼을 누르면 chatpGPTButton 버튼이 활성화된다.
    if st.button(label='날씨를 확인', key='weather'):
        
        #API를 호출한다.
        # 오늘의 날짜를 구한다. YYYYMMDD
        base_date = datetime.datetime.now().strftime('%Y%m%d')

        url=f"https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey=0k8h8kWmk0yI8FSQrbbh3gUNvgMzMjfKNAXR9iI%2FVOcaNDXJ5NwQOZTGo6S5dyZpQQ9ci%2BMQgAk2%2B1ygNybZfQ%3D%3D&pageNo=1&numOfRows=1000&dataType=JSON&base_date={base_date}&base_time=0630&nx=55&ny=127"
        response = requests.get(url)
        data = response.json()
        weather =get_sky_status_kor(data)

        st.session_state['content'] = f'오늘 점심 날씨 [{weather}]. 점심 메뉴 3 가지만 추천해줘'
        # print("weather button content: ", st.session_state['content'])
        #weather 을 화면에 출력한다.
        # st.write(st.session_state['content'])
    if st.session_state['content'] :
        st.write(st.session_state['content'])    

        #chatGPT에게 위 내용을 요청하는 버튼 생성
        if st.button(label ='클릭하여 chatGPT에게 위 내용을 요청',key='chatGPTButton'):
            # print("chatGPTButton button content: ", st.session_state['content'])
            #chatGPT에게 요청
            #인증 후
            openai.api_key = "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"
            #요청
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": st.session_state['content']}]
            )
            print(completion)
            #chatGPT의 응답을 화면에 출력
            st.write(f'chatGPT의 응답: {completion.choices[0].message.content}')


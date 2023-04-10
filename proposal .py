import streamlit as st
import openai


if 'background_textarea_value' not in st.session_state:
    st.session_state['background_textarea_value'] = ''
if 'point_value' not in st.session_state:
    st.session_state['point_value'] = ''
if 'chatGPT_callback' not in st.session_state:
    st.session_state['chatGPT_callback'] = ''    

st.title('chatGPT 제안서 작성')
st.write('FinanceData.KR - chatGPT API 활용를 참고했습니다.')
st.write('전체 url : https://financedata.notion.site/ChatGPT-6517d755152d40a99ae360a97e83b24c')


st.write('1. 배경과 상황을 설명합니다')
st.write('다음과 같은 제안요청서를 받았어')
st.session_state['background_textarea_value'] = st.text_area(label="[제안요청서-RFP] 내용을 붙여넣어 주세요 ")
st.write('일단 기억해줘')

if(st.session_state['background_textarea_value']):
    content = f"다음과 같은 제안요청서를 받았어 \n {st.session_state['background_textarea_value']} \n 일단 기억해줘"
    st.write(content)
    if st.button(label='[제안요청서 텍스트] 작성 후 chatGPT에서 문의하기', key=1):
        #chatGPT에게 요청0
        #인증 후
        openai.api_key = "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"
        #요청
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}]
        )
        print(completion)
        #chatGPT의 응답을 화면에 출력
        st.write(f'chatGPT의 응답: {completion.choices[0].message.content}')
        st.session_state['chatGPT_callback'] = True
    if(st.session_state['chatGPT_callback'] ):    
        st.write('위 내용 중에 어려운 내용은 별도로 chatGPT에게 물어보면서 알아두세요')

        st.write('2. 원하는 것이 무엇인지 설명합니다')
        st.write('원하는 것이 무엇인지(특히, 강조할 부분을) 명시 합니다. ')
        st.session_state['point_value'] = st.text_input(label="나는 시스템 구축에 있어서 기술적 우위를 강조하는 경쟁력 있는 제안서를 작성하려고 하려고해")
        if st.button(label='강조할부분 chatGPT에서 문의하기', key=2):
            st.session_state['chatGPT_callback'] = False
            content = st.session_state['point_value']
            #chatGPT에게 요청
            #인증 후
            # openai.api_key = "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"
            #요청
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": content}]
            )
            print(completion)
            #chatGPT의 응답을 화면에 출력
            st.write(f'chatGPT의 응답: \r\n {completion.choices[0].message.content}')
            st.session_state['chatGPT_callback'] = True

if(st.session_state['point_value'] and st.session_state['chatGPT_callback'] ):
    st.write('다음과 같은 목차로 작성할 예정이야')

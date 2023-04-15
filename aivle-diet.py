import openai
import streamlit as st

# OpenAI API 연결
openai.api_key = "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"

# OpenAI GPT-3 모델 설정
model_engine = "text-davinci-002"
prompt_template = "I am a personal nutritionist. Based on your current weight, height, age, activity level, dietary restrictions, and weight loss goals, I recommend the following diet plan: \n\nWeight: {} \nHeight: {} \nAge: {} \nActivity Level: {} \nDietary Restrictions: {} \nWeight Loss Goals: {} \nBMI: {} ({})\n\nDiet Plan:"

# 비만도 계산 함수
def calculate_bmi(weight, height):
    return weight / (height/100)**2

# 비만도 지수 그래프 함수
def plot_bmi(bmi):
    x = np.arange(5, 45, 0.1)
    y = [18.5, 23, 25, 30, 35, 40]
    labels = ['저체중', '정상체중', '과체중', '경도비만', '중증도비만', '고도비만']

    plt.plot(x, [18.5]*len(x), 'g--', label='저체중')
    plt.plot(x, [23]*len(x), 'y--', label='정상체중')
    plt.plot(x, [25]*len(x), 'r--', label='과체중')
    plt.plot(x, [30]*len(x), 'm--', label='경도비만')
    plt.plot(x, [35]*len(x), 'b--', label='중증도비만')
    plt.plot(x, [40]*len(x), 'k--', label='고도비만')
    plt.plot(bmi, 0, 'ro', markersize=10)
    plt.xlim(5, 45)
    plt.ylim(-1, 41)
    plt.xticks(y, labels)
    plt.xlabel('BMI')
    plt.ylabel('비만도 지수')
    plt.legend()
    st.pyplot()

# Streamlit 앱 구성
st.title("맞춤형 다이어트 계획 생성기")
weight = st.number_input("현재 체중(kg)", min_value=30.0, max_value=300.0, step=0.1)
height = st.number_input("키(cm)", min_value=100.0, max_value=300.0, step=0.1)
age = st.number_input("나이", min_value=5, max_value=120, step=1)
activity_level = st.selectbox("활동 수준", ["최소", "보통", "높음"])
dietary_restrictions = st.multiselect("식이 제한 사항", ["없음", "채식주의자", "유당 민감성", "과민성 대장 증후군"])
weight_loss_goals = st.multiselect("체중 감량 목표", ["1kg 이하", "1-2kg", "2-3kg", "3-4kg", "4kg 이상"])

if st.button("다이어트 계획 생성"):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        bmi_category = "저체중"
    elif bmi < 23:
        bmi_category = "정상"
    elif bmi < 25:
        bmi_category = "과체중"
    elif bmi < 30:
        bmi_category = "경도비만"
    elif bmi < 35:
        bmi_category = "중등도비만"
    else:
        bmi_category = "고도비만"
        
    prompt = prompt_template.format(weight, height, age, activity_level, dietary_restrictions, weight_loss_goals, round(bmi, 1), bmi_category)
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    diet_plan = response.choices[0].text
    st.success(diet_plan)


# 생성된 다이어트 계획 출력
st.subheader("나만의 맞춤형 다이어트 계획")
st.write(diet_plan)

# 비만도 지수 계산 및 그래프 출력
bmi = calculate_bmi(weight, height)
st.subheader("나의 비만도 지수")
st.write(f"현재 비만도 지수: {bmi:.2f}")
plot_bmi(bmi)

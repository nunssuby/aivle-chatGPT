# aivle-chatGPT

파일은 두개 (chatGPT-API.ipynb , front-chatGPT-API.py)

설치파일
```python
pip install -r requirements.txt
```

공통 설치 파일
pip install openai
pip install requests

1. chatGPT-API.ipynb
- 주피터노트북으로 실행
- 실행해보면 날씨를 받아온 input를 활용해서 chatGTP에게 요청

2. front-chatGPT-API.py
- streamlit 설치 (python 3.9.7에서 이슈가 있으므로 업데이트 필요, 잘 실행되면 그냥 진행)
  - pip install streamlit 
- 실행방법
  - streamlit run front-chatGPT-API.py
  
 3. proposal.py
 - 실행방법
  - streamlit run proposal.py
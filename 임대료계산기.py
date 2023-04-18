import streamlit as st
import datetime
from RentCalculator import *
from PIL import Image

fav = Image.open("favicon.ico")
st.set_page_config(page_title="임대료계산기", page_icon=fav)
st.title("임대료 계산기")

with st.form(key='main'):
    
    purpose = st.selectbox("**토지 구분**을 선택하세요. ", ("경작", "비경작"))
    area = st.number_input("**임대 면적**을 입력해주세요. (단위: m\u00b2)", format="%g", step=1, min_value=0)
    income = st.number_input("**단위면적당 농업 총수입**을 입력해주세요. (단위면적: m\u00b2)", format="%g", step=1, min_value=0)
    price = st.number_input("**개별 공시지가**를 입력해주세요. (단위면적: m\u00b2)", format="%g", step=1, min_value=0)
    start = st.date_input("**임대 시작일**을 입력해주세요.")
    end = st.date_input("**임대 종료일**을 입력해주세요.")

    submit = st.form_submit_button(label="**계산하기**")
    
if submit:
    rent = RentCalculator(purpose, area, income, price, start, end)
    if rent != None:
        st.write(f"임대료는 **{rent}원** 입니다.")
    else:
        st.write(f"임대 시작일과 종료일을 확인해주세요.")
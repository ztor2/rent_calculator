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
    income = st.number_input("**단위면적당 농업 총수입**을 입력해주세요. (22년 기준: 2401원, 단위면적: m\u00b2)", format="%g", step=1, min_value=0, value=2401)
    price = st.number_input("**개별 공시지가**를 입력해주세요. (단위면적: m\u00b2)", format="%g", step=1, min_value=0)
    start = st.date_input("**임대 시작일**을 입력해주세요.")
    end = st.date_input("**임대 종료일**을 입력해주세요.")

    submit = st.form_submit_button(label="**계산하기**")
    
if submit:
    rent = RentCalculator(purpose, area, income, price, start, end)
    if rent != None:
        st.write(f"<p style='font-size:19px;'>임대료는 <b>{rent}원</b> 입니다.</p>", unsafe_allow_html=True)
    else:
        st.write(f"임대 시작일과 종료일을 확인해주세요.")

st.write("")
st.write("")
st.write("")
st.markdown("*면적 및 개별공시지가는 부동산공시가격 알리미(<a href='www.realtyprice.kr'>www.realtyprice.kr) 에서 확인 가능합니다. <br/> **계산기를 통해 산출된 임대료값은 일반적인 상황(요율감면 등 불포함)을 가정하여 산출되었으므로 실제 임대료와 다를 수 있습니다.", unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import datetime
import time


st.header("신길중학교 배정 알리미", divider="rainbow")

df = pd.read_csv("data.csv")
df['생년월일'] = pd.to_datetime(df['생년월일'])

with st.container():
    st.write("이전학년 정보 입력")
    col1, col2, col3, col4  = st.columns(4)
    with col1 :
        grade_last = st.selectbox("이전학년", (1,2))
    with col2 :
        class_last = st.selectbox("이전반", (1,2,3,4,5,6,7,8,9))
    with col3 :
        num_last = st.number_input("이전번호",min_value=1, max_value=30, step=1)
    with col4 :
        name = st.text_input("이름")

    col5, col6, = st.columns(2)        
    
    with col5 :
        birth = st.date_input("생년월일 입력", value=datetime.date(2010, 1, 1))
    
    with col6 :
        pass
        
    button = st.button("확인")
        
    if button == True:
        data = df[ (df["이전학년"]==grade_last) & (df["이전반"]==class_last) & (df["이전번호"]==num_last) & (df["이름"]==name)]
        progress_text = "처리중입니다."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
                
        if len(data)==0:
            st.warning("요청하신 정보를 찾을 수 없습니다.")
        else : 
            date = data["생년월일"][0].date()
            diff = date-birth

            if diff.days ==0 :
                
                st.warning(f':blue[{data["이름"][0]}]님은 {data["신학년"][0]}학년 {data["신반"][0]}반 {data["신번호"][0]}번에 배정되었습니다.')
            else:
                st.warning("요청하신 정보를 찾을 수 없습니다.")
        
    
        
        
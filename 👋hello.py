import streamlit as st
from PIL import Image
image = Image.open('uteicon.jpg')
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

mid, col2 = st.columns([1,5 ])
with mid: st.image(image, width=100)
with col2:
    st.write('###  HCMC University of Technology and Education')


st.write("# Welcome to Movie Recommender System! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Build a Machine Learning web application in Python with Streamlit. 
    **A content based movie recommender system using cosine similarity.**
    
    ### How to run this application
    - Select model
    - After the model is created, select app to run
    ### Student
    - Nguyễn Sinh Hùng
    - 20110647
    ### Teacher
    - Trần Tiến Đức
    ### Source code
    - https://github.com/e22313/machinelearning.git
    ### Reference
    - https://www.youtube.com/watch?v=1xtrIEwY_zY
    - https://www.datacamp.com/tutorial/streamlit
"""
)
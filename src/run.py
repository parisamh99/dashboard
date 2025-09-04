
import streamlit as st
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

banner = Image.open('data/images.jpeg')
st.image(banner)
st.title(':zap: Dashboard')

login_option = st.sidebar.radio('Login/Singup', ('Login', 'Singup'))
if login_option == 'Login':
    with st.sidebar.form("login"):
        st.write("Login Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("signup"):
        st.write("Singup Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Singup")
        if submitted:
            pass



with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)
    

with st.expander('user profile:'):
    col1, col2 = st.columns(2)
    col1.text_input('name:')
    col2.text_input('location:')
    st.camera_input('camera input', key='camera_input')    





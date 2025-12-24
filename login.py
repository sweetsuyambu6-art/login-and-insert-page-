import streamlit as st
import pandas as pd
import hashlib

st.title("Long-in")
#input longin user and  password 
name=st.text_input("USER NAME")
user_name =st.text_input("User Name")
if user_name == "guvi@gmail.com":
   st.success(f"{user_name}successful")
elif user_name == (f"{user_name}error") :
   st.success("error")
#input password 
password = st.text_input("Password", type="password")
password=hashlib.sha256("guvi@123".encode()).hexdigest()

if st.button('login'):
    st.success(f"{name} have login successful")

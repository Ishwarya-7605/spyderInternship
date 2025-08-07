import streamlit as st
with st.form("signup"):
   st.title("Welcome to Spyder Academy")
   st.header("welcome to signup page")
Username=st.text_input("Username")
Password=st.text_input("Password") 
Confirm_Password=st.text_input("Confirm password")
if st.button("signup"):
   if(Password==Confirm_Password):
      st.success("sign up successfully")
   else:  
      
      if st.form("signup"):  
         st.title("login")
with st.form("login"):
   st.header("welcome to login page")
   Username=st.text_input("Username")
   Password=st.text_input("Password")
   if st.button("Login"):
    if Username==Username and Password==Password:
      st.success(f"Login Successfully. welcome {Username}!!")
    else:
       st.error("Try Again Later")       
import streamlit as st
import google.generativeai as genai
import os

# Streamlit Secrets ကနေ API Key ကို ယူခြင်း
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Assistant", layout="centered")
st.title("🤖 ကျွန်ုပ်၏ AI လက်ထောက်")
st.write("သင် သိလိုသမျှကို မေးမြန်းနိုင်ပါတယ်။")

# User ရိုက်မယ့်နေရာ
user_input = st.text_input("မေးခွန်းရိုက်ပါ...", placeholder="ဒီမှာ ရိုက်ပါ...")

if st.button("အဖြေတောင်းမယ်"):
    if user_input:
        with st.spinner('ခဏစောင့်ပါ...'):
            response = model.generate_content(user_input)
            st.success("AI ရဲ့ အဖြေ:")
            st.write(response.text)
    else:
        st.warning("စာသားတစ်ခုခု အရင်ရိုက်ထည့်ပါ")
Sent
Write to Baba Bu



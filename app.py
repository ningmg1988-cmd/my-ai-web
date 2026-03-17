import streamlit as st
import google.generativeai as genai

# API Key ကို Secrets ထဲကနေ ယူခြင်း
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # ရှေ့မှာ models/ ထည့်ရပါမယ်
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
except Exception as e:
    st.error("API Key သတ်မှတ်ရာတွင် အမှားရှိနေပါသည်။")

st.set_page_config(page_title="AI Assistant", layout="centered")
st.title("🤖 ကျွန်ုပ်၏ AI လက်ထောက်")
st.write("သင် သိလိုသမျှကို မေးမြန်းနိုင်ပါတယ်။")

user_input = st.text_input("မေးခွန်းရိုက်ပါ...", placeholder="ဒီမှာ ရိုက်ပါ...")

if st.button("အဖြေတောင်းမယ်"):
    if user_input:
        with st.spinner('ခဏစောင့်ပါ...'):
            try:
                response = model.generate_content(user_input)
                st.success("AI ရဲ့ အဖြေ:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error တက်နေပါတယ်: {e}")
    else:
        st.warning("စာသားတစ်ခုခု အရင်ရိုက်ထည့်ပါ")


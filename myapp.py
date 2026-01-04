import streamlit as st
import yfinance as yf

# إعدادات واجهة الموبايل
st.set_page_config(page_title="Crypto Ali", layout="centered")

st.title("💰 متابع الكريبتو - علي")

# قائمة اختيار العملة
option = st.selectbox(
    'اختر العملة التي تود متابعتها:',
    ('BTC-USD', 'ETH-USD', 'SOL-USD'))

# جلب بيانات السعر
ticker = yf.Ticker(option)
price = ticker.history(period="1d")['Close'].iloc[-1]

# عرض السعر بشكل جذاب
st.metric(label=f"السعر الحالي لـ {option}", value=f"${price:,.2f}")

st.success("التطبيق يعمل بنجاح على سحابة ستريملت!")

import streamlit as st
import ccxt

st.title("Crypto Data Live")

# الاتصال بمنصة Kraken (تعمل عادة بدون قيود جغرافية)
try:
    exchange = ccxt.kraken() 
    symbol = 'BTC/USDT'
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']
    
    st.metric(label=f"سعر {symbol} (Kraken)", value=f"${price:,.2f}")
    st.success("تم جلب البيانات بنجاح!")
except Exception as e:
    st.error(f"حدث خطأ: {e}")


import streamlit as st
import ccxt

st.title("Crypto Data Live")

# Fetch data
try:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USDT')
    price = ticker['last']
    st.metric(label="BTC/USDT", value=f"${price:,.2f}")
except Exception as e:
    st.error(f"Error: {e}")

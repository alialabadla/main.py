import ccxt

st.title("بيانات كريبتو حية (CCXT)")

‎# جلب بيانات من منصة Binance
try:
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    ticker = exchange.fetch_ticker(symbol)
    
    st.metric(label=f"سعر {symbol} الآن", value=f"${ticker['last']:,.2f}")
    st.write(f"أعلى سعر اليوم: {ticker['high']}")
    st.write(f"أدنى سعر اليوم: {ticker['low']}")
except Exception as e:
    st.error(f"خطأ في جلب البيانات: {e}")
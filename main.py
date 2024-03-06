import streamlit as st
import time
import yfinance as yf
import streamlit as st
import pandas as pd

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()




st.write("""
 # Stock Price App

Shown are the stock **closing price** and volume of 
1. TCS
2. Infosys
[I'm an inline-style link](https://www.google.com)
""")
tickerSymbol='TCS.ns'



tickerData=yf.Ticker(tickerSymbol)
info=tickerData.mutualfund_holders
st.write("It is owned by follwoing mutual fund companies ",info)
tickerDf=tickerData.history(period='1d',start='2020-5-31',end='2023-4-3')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.button("Rerun")
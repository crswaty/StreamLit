import yfinance as yf
import streamlit as st
import datetime
from datetime import date

# run with "streamlit run StockApp.py" in local terminal
# run pipreqs command from within directory to create requirements file automatically

st.write("""
# Stock Price App

## Shown are the stock closing price and volume of Google

### User inputs 
""")

tickersym = st.text_input(label='What ticker do you want?',value='GOOGL')
date_start = st.date_input(label="What start date would you like?", value=datetime.date(2022, 1, 1))
date_end = st.date_input(label="What end date would you like?", value=date.today())

# tickersym = 'GOOGL'
tickerdat = yf.Ticker(tickersym)
tickerdf = tickerdat.history(period='1d', start=date_start, end=date_end)

st.write('''
**Closing price** chart for selected dates
''')

st.line_chart(tickerdf.Close)

st.write('''
**Volume chart** for selected dates
''')

st.line_chart(tickerdf.Volume)
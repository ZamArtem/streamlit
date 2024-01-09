import yfinance as yf
import streamlit as st 
import pandas as pd

def stock_init(self,sor):
    symbol,name,lastsale,netchange,change,marketcap,country,year,volume,sector,industry = sor.strip().split(",")
    self.symbol     = symbol
    self.name       = name
    self.lastsale   = lastsale
    self.netchange  = netchange
    self.change     = change
    self.marketcap  = marketcap
    self.country    = country
    self.year       = year
    self.volume     = volume
    self.sector     = sector
    self.industry   = industry

Stock = type("Stock", (), {
    "__init__": stock_init,
})


with open("stock.csv")as f:
    lista = [Stock(sor) for sor in f]


ticker_symbol = st.selectbox('Select',([sor.symbol for sor in lista]))


st.write(f"""
{ticker_symbol}
""")

datest   = st.date_input("Start",value=None)
date_end = st.date_input("End",value=None)
ticker_data     = yf.Ticker(ticker_symbol) 

ticker_df = ticker_data.history(period="1d", start=datest, end=date_end)

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)
import streamlit as st
import pandas as pd
import datetime as dt
import plotly
import yfinance as yf
import concurrent.futures
from pathlib import Path
import time
import numpy as np
import itertools as it

pd.options.plotting.backend = 'plotly'

# --- import csv of Yahoo Tickers ---
@st.cache
def get_tickers_list():
    with open("images/tickers_list.csv", 'r') as f:
    	tickers = pd.read_csv(f)
    return tickers

# --- Equities Data pull from Yahoo Finance based on User Selections ---
@st.cache
def pull_yf(tickers, startDate, endDate):
	OHLC_list = []
	for i in tickers:
	    base = yf.Ticker(i)
	    OHLC = base.history(start=startDate, end=endDate).reset_index()[['Date','Close']]
	    OHLC['Date'] = OHLC['Date'].dt.date
	    OHLC['ticker'] = i
	    OHLC_list.append(OHLC)

	df = pd.concat(OHLC_list)
	return df

# --- Cryptos Data pull from Glassnode script output ---
@st.cache
def get_crypto_prices():
    with open("images/historical_crypto_prices.csv", 'r') as f:
    	df = pd.read_csv(f)
    	df = df[['Date', 'Close', 'ticker']]
    	df['Date'] = pd.to_datetime(df['Date']).dt.date

    return df

crypto_data =  get_crypto_prices()

tickers = get_tickers_list()['Symbol']



# --- Add Headline to Webpage ---
st.title("Correlation Calculator!")
st.write(
            "This tab is still in testing!"
        )
st.write('---')
st.write('#')


# --- Prompt User for Asset, Start Date, End Date Selections ---
stock_options = st.multiselect(
    		'Select Stock Tickers:',
    		tickers)

crypto_options = st.multiselect(
    		'Select Crypto Symbol:',
    		crypto_data['ticker'].unique())

with st.container():
	left_column, right_column = st.columns(2)
	with left_column:
		startDate = st.date_input(
		    "Select a start date:",
		    dt.date(2009, 1, 3),
		    max_value = dt.date.today())
	with right_column:
		endDate = st.date_input(
		    "Select a end date:",
		    dt.date.today())



if len(stock_options) + len(crypto_options) < 2:
    st.warning('Please select at least two assets to run the calculator.')
# @st.cache
# def pull_cryptos(symbols, startDate, endDate):


if len(stock_options) + len(crypto_options) > 1:
	stock_df = pull_yf(stock_options, startDate, endDate)
	crypto_df = crypto_data[crypto_data['ticker'].isin(crypto_options)]
	big_df = pd.concat([crypto_df,stock_df])
	big_df = big_df.pivot(values='Close', columns = 'ticker', index = 'Date')

	adjusted_df = big_df.pct_change()
	df_corr = adjusted_df.corr()

	rolling = pd.DataFrame(index = adjusted_df.index)

	col_pairs = list(it.combinations(big_df.columns, 2))

	for pair in col_pairs:
    # select the first three letters of each name of the pair
	    corr_name = f"{'-'.join(pair)}"
	    rolling[corr_name] = adjusted_df[list(pair)[0]].rolling(min_periods=1, window=30).corr(adjusted_df[list(pair)[1]])#.iloc[0::2, -1].reset_index(drop=True)
	

	fig = plotly.graph_objects.Figure()
	fig.add_trace(
    plotly.graph_objects.Heatmap(
        x = df_corr.columns,
        y = df_corr.index,
        z = np.array(df_corr),
        text=df_corr.values,
        texttemplate='%{text:.2f}',
        #title= "Correlation Matrix"
    )
)
	#st.write(adjusted_df[adjusted_df.index >= startDate])
	#st.write(rolling[rolling.index >= startDate])
	st.write(rolling[rolling.index >= startDate].plot(title= 'Rolling 30 Day Correlation'), layout_xaxis_range=[startDate, endDate]) #, xlim= (startDate, endDate)))
	st.write(adjusted_df.plot(title= 'Daily Percentage Price Change'))
	st.write(big_df.plot(title= 'Daily Price (usd)'))
	st.write(fig)










#st.button('Run', on_click=change_session_state)

#--- Progress bar code --- 
	# my_bar = st.progress(0)

	# for percent_complete in range(100):
	#     time.sleep(0.1)
	#     my_bar.progress(percent_complete + 1)


















# if len(stock_options) + len(crypto_options) < 2:
#     st.warning('Please select at least two assets to run the calculator.')
# # @st.cache
# # def pull_cryptos(symbols, startDate, endDate):


# #if len(stock_options) + len(crypto_options) > 1:
# 	#stock_df = pull_yf(stock_options, startDate, endDate)
# 	#crypto_df = crypto_data[crypto_data['ticker'].isin(crypto_options)]
# if (len(crypto_options) > 0) & (len(stock_options) > 0):  
# 	stock_df = pull_yf(stock_options, startDate, endDate)
# 	crypto_df = crypto_data[crypto_data['ticker'].isin(crypto_options)]
# 	big_df = pd.concat([crypto_df,stock_df])
# elif len(crypto_options) > 0:
# 	crypto_df = crypto_data[crypto_data['ticker'].isin(crypto_options)]
# 	big_df = crypto_df
# else: 
# 	stock_df = pull_yf(stock_options, startDate, endDate)
# 	big_df = stock_df
# 	big_df = big_df.pivot(values='Close', columns = 'ticker', index = 'Date')

# big_df['Date'] = pd.to_datetime(big_df['Date']) 

# adjusted_df = big_df.pct_change()
# st.write(adjusted_df)


import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data visualization
import plotly.graph_objs as go

data = yf.download(tickers='AAPL', period='5d', interval='5m')
print(data)

fig = go.Figure()
fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], 
                             name = 'Market Data'))

fig.update_layout(title='AAPL live Share', yaxis_title='Stock Price')

fig.update_xaxes(rangeslider_visible = True,
                 rangeselector=dict(
                     buttons=list([
                         dict(count=15, label='15m', step='minute',stepmode='backward'),
                         dict(count=45, label='45m', step='minute',stepmode='backward'),
                         dict(count=1, label='HTD', step='hour',stepmode='todate'),
                         dict(count=3, label='3h', step='hour',stepmode='backward'),
                         dict(step='all')
                         ])
                     )
                 )



fig.show()
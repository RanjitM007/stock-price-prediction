import yfinance as yf

# Fetch the components of S&P 500
sp500 = yf.Ticker('^GSPC')
sp500_components = sp500.components
print(sp500_components)
from yahoofinance import HistoricalPrices

req = HistoricalPrices("AAPL", "2024-7-20", "2024-7-27")
print(type(req))
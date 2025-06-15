from .market_data_provider import MarketDataProvider
import yfinance as yf

class YFinanceProvider(MarketDataProvider):
    def get_price(self, symbol: str) -> float:
        data = yf.Ticker(symbol)
        price = data.history(period="1d").tail(1)["Close"].values[0]
        return float(price)

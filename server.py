import yfinance as yf
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("yfinanceserver")
@mcp.tool()
def prices(stock_ticker: str) -> str:
    """This tool returns the last known price for a given stock ticker.
    Args:
        stock_ticker: an alphanumeric stock ticker
        Example payload: "AAPL"
    Returns:
        str: "Ticker: LastPrice"
        Example Response: "AAPL: $208.45"
    """
    ticker = yf.Ticker(stock_ticker)
    historical_prices = ticker.history(period='1mo')
    last_month_closes = historical_prices['Close']
    return stock_ticker + ": " + str(last_month_closes.iloc[-1])

if __name__ == "__main__":
    mcp.run(transport="stdio")
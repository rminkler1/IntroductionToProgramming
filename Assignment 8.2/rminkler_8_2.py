# Robert Minkler
# July 5, 2024
# Assignment 8.2

# Create a dictionary of at least 10 stocks. ticker: stock price
# Prompt the user for a ticker symbol. When found show the ticker symbol and stock price.
# If not found display an error message.

# Build dictionary with stock prices and tickers

# CONSTANTS
STOCKS = {
    'VOO': 509.37,
    'AMZN': 199.81,
    'BRK.A': 618000.00,
    'BRK.B': 409.97,
    'GOOG': 192.11,
    'MSFT': 467.38,
    'V': 269.96,
    'NVDA': 126.84,
    'AAPL': 225.15,
    'TSM': 183.30,
    'INTC': 31.86,
    'XOM': 113.02,
}

# Build a dictionary of stock names. I could have done this with a single dictionary ticker: [price, 'name']
# This is extra because I want to stay within the program requirements for the assignment. ticker: price
STOCK_NAMES = {
    'VOO': 'Vanguard S&P 500 ETF',
    'AMZN': 'Amazon.com Inc',
    'BRK.A': 'Berkshire Hathaway Inc Class A',
    'BRK.B': 'Berkshire Hathaway Inc Class B',
    'GOOG': 'Alphabet Inc Class C',
    'MSFT': 'Microsoft Corp',
    'V': 'Visa Inc',
    'NVDA': 'NVIDIA Corp',
    'AAPL': 'Apple Inc',
    'TSM': 'Taiwan Semiconductor Mfg. Co. Ltd.',
    'INTC': 'Intel Corp',
    'XOM': 'Exxon Mobil Corp',
}


def main():
    # Display available tickers to the user since there are only 12.
    print_tickers()

    # Get stock ticker from user. Return ticker, name, and price.
    ticker, stock_name, stock_price = get_stock_info()

    # Display the results
    print(f'{ticker} - {stock_name}: ${stock_price:.2f}')


def get_stock_info():
    """
    Prompts the user for a stock ticker. Retrieves the price and company name.
    Returns ticker, stock_name, stock_price
    """

    # Run this loop prompting for a ticker until a valid ticker is entered.
    while True:
        # Prompt user for a ticker symbol. Convert it to all uppercase to match ticker symbols
        user_ticker = input('Enter a ticker symbol to see its value: ').upper()

        # Get the stock price
        stock_price = STOCKS.get(user_ticker)

        # Get the stock name
        stock_name = STOCK_NAMES.get(user_ticker)

        # Validate results. Exit loop if valid.
        if stock_price is None or stock_name is None:
            # Show error if ticker is not found
            print(f'The ticker, {user_ticker} was not found. Please enter a different stock ticker.')
        else:
            # Exit the loop if stock data was found. Return results
            return user_ticker, stock_name, stock_price


def print_tickers():
    """
    Display all tickers available from the dictionary.
    """
    # Show available ticker symbols
    print(f'Available tickers include: ', end='')

    # initialize i as an index to track the number of items read from the dictionary.
    i = 0

    # print each ticker symbol.
    for ticker in STOCKS.keys():
        if (len(STOCKS) - 1) > i:
            # print with a comma unless it is the last ticker
            print(ticker, end=', ')
        else:
            # on the last ticker end with a period and new line
            print(ticker, end='.\n')

        # iterate i to track how many dictionary items we have printed
        i += 1


if __name__ == '__main__':
    main()

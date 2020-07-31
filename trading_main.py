# Import the libraries we need
import os
import datetime as dt
from datetime import date
import time
import pandas_datareader.data as web


# Function to get the data
def get_data_dump(tickers, start, end):

    # Need a folder
    if not os.path.exists('E:\\stocks_data'):
        os.makedirs('E:\\stocks_data')

    for ticker in tickers:
        print(ticker)
        # 20 second sleep, so we dont get blocked for hoggin the servers
        time.sleep(20)
        if not os.path.exists('E:\\stocks_data/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('E:\\stocks_data/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


# The variables
tickers = ['BKNG', 'AMZN', 'NVR', 'AZO', 'GOOGL']
start = dt.datetime(2000, 1, 1)
end = date.today()


# Run the functions as needed
#get_data_dump(tickers, start, end)

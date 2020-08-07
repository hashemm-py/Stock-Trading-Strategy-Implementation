# Import the libraries we need
import os
import datetime as dt
from datetime import date, timedelta
import time
import pandas_datareader.data as web
import pandas as pd


# All functions
# Function to get the data
def get_data_dump(tickers, start, end, folder_path):

    # Need a folder
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for ticker in tickers:
        print(ticker)
        
        # 20 second sleep, so we dont get blocked for hoggin the servers
        time.sleep(20)
        if not os.path.exists(folder_path + '/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv(folder_path + '/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


# Function to update the latest data
def update_latest_data(end, updatedays, folder_path):
    temp_folder_path = folder_path + '\\temp'

    # Get the missing data
    start = end - timedelta(days=updatedays)
    get_data_dump(tickers, start, end, temp_folder_path)

    #Getting the name of the files
    not_found = []
    entries = os.listdir(temp_folder_path)
    for entry in entries:
        try:
            print(entry)
            df_old = pd.read_csv(folder_path + '\\' + entry)
            df_new = pd.read_csv(temp_folder_path + '\\' + entry)

            # Delete last two entries (to get any updates which we might have missed)
            df_old = df_old[~df_old.Date.str.contains(str(start))]
            df_old = df_old[~df_old.Date.str.contains(str(start + timedelta(days=1)))]

            # Update the data
            df = df_old.append(df_new)
            df.to_csv(folder_path + '\\' + entry)

        except Exception as e:
            print(e)
            print('Did not find ' + entry)
            not_found.append(entry)
            continue
    #print(not_found)
    #not_found.to_csv(new_path + '\\' + 'Not_Found.csv')


# The variables
tickers = ['BKNG', 'AMZN', 'NVR', 'AZO', 'GOOGL']
# Dates for full data dump
#start = dt.datetime(2000, 1, 1)
# While running the update_latest_data No Start Date is required
end = date.today()
folder_path = 'E:\\stocks_data'
updatedays = 8

# Run the functions as needed
#get_data_dump(tickers, start, end, folder_path)
update_latest_data(end, updatedays, folder_path)

import psycopg2
import os
import pandas as pd
from datetime import datetime
from io import StringIO
import csv
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', 
                    format='%(name)s - %(levelname)s - %(message)s')


def list_files(directory):
    files = []
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            files.append(file_name)
    return files

if __name__ == "__main__":
    # TODO: Change the index name here based on the folder names
    indexName = "sp500"

    directory_path = "./Data/"+ indexName + "/csv"
    file_list = list_files(directory_path)
    
    """
    DO NOT USE DATABASE CONNECTION THIS WAY IN PRODUCTION.
    FOR DEVELOPMENT PURPOSES ONLY.
    """
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="stockmarketquote",
        user="<DB_USERNAME>",
        password="<DB_PASSWORD>"
    )
    
    starttime = datetime.now()
    try:
        for file_name in file_list:
            tickername = file_name.replace(".csv", "")
            filepath = directory_path + "/" + file_name
        
            data = pd.read_csv(filepath)
            # We're appending the ticker name into the table
            data = data.assign(tickername=tickername)

            sio = StringIO()
            writer = csv.writer(sio)
            writer.writerows(data.values)
            sio.seek(0)
            with conn.cursor() as c:
                c.copy_from(
                    file=sio,
                    table=indexName,
                    columns=[
                        "tradingday",
                        "low",
                        "openprice",
                        "volume",
                        "high",
                        "closeprice",
                        "adjustedclose",
                        "tickername"
                    ],
                    sep=","
                )
            conn.commit()
    except Exception as e:
        logging.error(f"ERROR: {e}")
        pass ## We catch the errors in the logfile to analyse later.

    endtime = datetime.now()
    print(f"Total time taken for the operation: {endtime - starttime}")
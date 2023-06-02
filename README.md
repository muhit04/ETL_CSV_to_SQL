### Datasource: https://www.kaggle.com/datasets/paultimothymooney/stock-market-data

Get a feel for the data
There are two file types CSV and JSON. 
We will be using CSV for our data source because JSON can sometimes be a little messy to deal with.

### Folder structure

    | Data\
    |   forbes200\
    |       csv\
    |   nasdaq\
    |       csv\
    |   nyse\
    |       csv\
    |   sp500\
    |       csv\
    |   allTheSql.sql
    |   app.log
    |   insertQuery.py
    |   pyproject.toml
    |   README.md

With basic "head" command in unix we can have a look at the data.

    $ head ATAX.csv

    Date,Low,Open,Volume,High,Close,Adjusted Close
    31-03-1986,47.50410461425781,47.50410461425781,0,49.879310607910156,47.50410461425781,2.5686941146850586
    01-04-1986,51.06691360473633,51.06691360473633,11367,53.44211959838867,51.06691360473633,2.7613489627838135
    

We can already see the data is strcutured and nicely formatted. (check a couple of different files to ensure). LRCS.csv has some data inconsistencies, we're catching the errors in a log file, because we don't own the data, it's hard to know what values will replace them (there're not many). In a real situations, we can analyze the error from the logs and maintain a proper data integration and consistency. However, for our purpose, we will just simply ignore them. 

It has the following columns -> Date, Low, Open, Volume, High, Close, Adjusted Close. 

At this point, we can assume it's a good idea for a SQL Database like Postgresql/MySQL. There are several ways to design our schema, we will keep it simple and each index will have their own table. We will create an extra column for the ticker names i.e. AAPL, NDAQ etc.


To connect to our postgresql

    psql -U postgres -h localhost -p 5432

To run the sql commands directly from a file

    psql -U postgres -h localhost -p 5432 -f /path/to/sqlfile.sql

It took the following time to finish our ETL:
    Nasdaq: 
        Total time taken for the operation: 0:01:04.598601
        No. of Rows:  2,613,168
    Forbes2000:
        Total time taken for the operation: 0:02:23.653159
        No. of Rows: 5,601,971
    NYSE:
        Total time taken for the operation: 0:02:59.275489
        No. of Rows: 6,994,408
    SP500:
        Total time taken for the operation: 0:01:19.837416
        No. of Rows: 3,266,000


    Total time: 7m45s
    Total records: 18,435,547

Local Dev Specs
Intel 8th Gen Core i3
8 GB RAM
 
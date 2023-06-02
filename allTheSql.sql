CREATE DATABASE stockmarketquote;

\c stockmarketquote;

CREATE TABLE nasdaq (
    id SERIAL PRIMARY KEY,
    tradingday DATE,
    low REAL,
    openprice REAL,
    volume REAL,
    high REAL,
    closeprice REAL,
    adjustedclose REAL,
    tickername TEXT,
    UNIQUE (tickername, tradingday)
);

CREATE TABLE forbes2000 (
    id SERIAL PRIMARY KEY,
    tradingday DATE,
    low REAL,
    openprice REAL,
    volume REAL,
    high REAL,
    closeprice REAL,
    adjustedclose REAL,
    tickername TEXT,
    UNIQUE (tickername, tradingday)
);

CREATE TABLE nyse (
    id SERIAL PRIMARY KEY,
    tradingday DATE,
    low REAL,
    openprice REAL,
    volume REAL,
    high REAL,
    closeprice REAL,
    adjustedclose REAL,
    tickername TEXT,
    UNIQUE (tickername, tradingday)
);

CREATE TABLE sp500 (
    id SERIAL PRIMARY KEY,
    tradingday DATE,
    low REAL,
    openprice REAL,
    volume REAL,
    high REAL,
    closeprice REAL,
    adjustedclose REAL,
    tickername TEXT,
    UNIQUE (tickername, tradingday)
);


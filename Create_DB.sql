DROP DATABASE IF EXISTS CCDB;
CREATE DATABASE CCDB;

USE CCDB;

CREATE TABLE Bitcoin
(
  the_date			DATETIME        NOT NULL,
  pirce_open		FLOAT,
  pirce_close		FLOAT,
  pirce_high		FLOAT,
  pirce_low			FLOAT,
  
  PRIMARY KEY (the_date)
);

CREATE TABLE Dogecoin
(
  the_date			DATETIME        NOT NULL,
  pirce_open		FLOAT,
  pirce_close		FLOAT,
  pirce_high		FLOAT,
  pirce_low			FLOAT,
  
  PRIMARY KEY (the_date)
);

CREATE TABLE Ethereum
(
  the_date			DATETIME        NOT NULL,
  pirce_open		FLOAT,
  pirce_close		FLOAT,
  pirce_high		FLOAT,
  pirce_low			FLOAT,
  
  PRIMARY KEY (the_date)
);

CREATE TABLE Bitcoin_Historical
(
  the_date			DATETIME        NOT NULL,
  pirce				FLOAT,
  
  PRIMARY KEY (the_date)
);

CREATE TABLE Dogecoin_Historical
(
  the_date			DATETIME        NOT NULL,
  pirce				FLOAT,
  
  PRIMARY KEY (the_date)
);

CREATE TABLE Ethereum_Historical
(
  the_date			DATETIME        NOT NULL,
  pirce				FLOAT,
  
  PRIMARY KEY (the_date)
);



-- creates the database hbtn_0d_usa and the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT UNIQUE AUTO GENERATED NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
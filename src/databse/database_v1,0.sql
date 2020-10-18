CREATE DATABASE secom;

USE secom; 

CREATE TABLE users(
    user_id INT(10) PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(20) NOT NULL,
    pswd VARCHAR(80) NOT NULL,
    hint VARCHAR(30) NOT NULL,
    user_type INT(2) NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    second_name VARCHAR(30) NOT NULL,
    f_last_name VARCHAR(30) NOT NULL,
    m_last_name VARCHAR(30) NOT NULL
);
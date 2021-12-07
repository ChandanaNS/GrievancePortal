-- Create Database
CREATE DATABASE OGMP;

USE OGMP;

-- User table
CREATE TABLE IF NOT EXISTS users (
    UserID INT(11) AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(255),
    UserName VARCHAR(200),
    Password LONGTEXT ,
    Email VARCHAR(50),
    Gender varchar(50) ,
    DateofBirth DATE,
    PhoneNumber varchar(50),
    Grievances longtext
)  ENGINE=INNODB;

-- Grievance table
CREATE TABLE IF NOT EXISTS grievance (
    GrievanceID INT(11) AUTO_INCREMENT PRIMARY KEY,
    GrievanceCategory VARCHAR(100) NOT NULL,
    GrievanceStatus VARCHAR(100) NOT NULL,
    Description VARCHAR(255),
    RaisedUser VARCHAR(255),
    Reply VARCHAR(255)
)  ENGINE=INNODB;

-- Other Queries

-- SELECT * from OGMP.users ;
-- SELECT Grievances FROM OGMP. users where UserID=2;
-- select * from OGMP.grievance where RaisedUser='mon';
-- SELECT * FROM  OGMP.users where UserName='mon';
-- update users set OrderedProducts='{0}' where UserName='{1}';
-- SELECT * FROM grievance ORDER BY GrievanceID DESC LIMIT 1;
-- select * from GroceryGo.users;
-- select * from OGMP.grievance where GrievanceID=4;
-- update grievance set Description="new"where GrievanceID=4;
-- SELECT * FROM grievance WHERE RaisedUser='mon'

CREATE DATABASE StudentDB;
GO

USE StudentDB;

CREATE TABLE Students (
    student_id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    age INT,
    course NVARCHAR(50),
    marks INT
);

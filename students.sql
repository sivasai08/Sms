-- StudentDB Database Schema

-- Create Students table
CREATE TABLE Students (
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    age INT NOT NULL,
    course NVARCHAR(100) NOT NULL,
    marks INT NOT NULL
);

-- Insert sample data (optional)
INSERT INTO Students (name, age, course, marks) VALUES
('John Doe', 20, 'Computer Science', 85),
('Jane Smith', 22, 'Mathematics', 92),
('Bob Johnson', 21, 'Physics', 78);

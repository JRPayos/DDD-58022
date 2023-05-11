create database Student;

select *from student.students_info;

-- all records residing Laguna--
SELECT *FROM student.students_info WHERE city ='Laguna';

-- all students records with sem grade --
SELECT *FROM student.students_info WHERE sem_grade='80';

-- all female students records --
SELECT *FROM student.students_info WHERE gender ='F';

-- all student record with youngest entry age
SELECT *FROM student.students_info WHERE entry_age = '17';
SELECT MIN(entry_age) AS min_age FROM student.students_info;

-- all student's records with the highest final_exam 
SELECT *FROM student.students_info WHERE final_exam= '100';
SELECT MAX(final_exam) AS highest_final_exam FROM student.students_info;

-- all student's records who are not 4th year
SELECT *FROM student.students_info WHERE NOT status = '4TH YEAR';

-- sort/arrange all student's records according to their sem_grade(descending)
SELECT *FROM student.students_info ORDER BY sem_grade DESC;

-- all student's records who are Male and 1st year
SELECT *FROM student.students_info WHERE gender ='M' AND status= '1ST YEAR';

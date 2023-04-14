create database emp_database;
create table emp_databse.EMP_1(EMP_NUM char(3), EMP_LNAME varchar(15), EMP_FNAME varchar(15), EMP_INITIAL char(1), EMP_HIREDATE date, JOB_CODE char(3), primary key (EMP_NUM)); 

insert into emp_databse.EMP_1(EMP_NUM, EMP_LNAME, EMP_FNAME, EMP_INITIAL, EMP_HIREDATE, JOB_CODE) 
values	(001, 'Wayne', 'Bruce', 'B', '2022-11-20', '501'),
		(002, 'Kent', 'Clark', 'S', '2023-03-09', '502'),
        (003, 'Falcone', 'Carmine', 'D', '2022-08-13', '500'),
		(004, 'Dent', 'Harvey', 'K', '2022-11-20', '501'),
		(005, 'Kyle', 'Selina', 'L', '2023-03-09', '502'),
		(006, 'Quinzel', 'Harleen', 'F', '2023-03-09', '502'),
		(007, 'Gordon', 'James', 'W', '2023-03-09', '502');
		
        
select* from emp_databse.EMP_1;


select* from emp_databse.EMP_1 where JOB_CODE = 502;
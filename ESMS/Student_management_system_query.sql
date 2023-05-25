-- admin database table
create database sms;

-- table record for admin
create table sms.admin_sms 
(admin_id int not null auto_increment primary key, 
admin_username varchar(40) not null, 
admin_password varchar(40) not null);

insert into sms.admin_sms(admin_id, admin_username,admin_password)
values ('1', 'root', 'root'); 

select *from sms.admin_sms;

-- table for student records
create table sms.student_accounts
(student_id int not null primary key, 
first_name varchar(40) not null, 
middle_name varchar(40) not null, 
last_name varchar(40) not null,
department varchar(40) not null,
course_program varchar(40) not null,
birthdate datetime not null,
sex varchar(6) not null);

select *from sms.student_accounts;
create database ABC_Computer;

create table ABC_Computer.Computer_Table
(SerialNumber int primary key, 
Make varchar(12) , 
Model varchar(24),
ProcessorType varchar(24),
ProcessorSpeed double (3,2),
MainMemory varchar(15),
DiskSize varchar(15));

insert into ABC_Computer.Computer_Table (SerialNumber, Make, Model, ProcessorType, ProcessorSpeed, MainMemory, DiskSize)
values	(9871234, 'HP', 'Pavilion 500-210qe', 'Intel i5-4530', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
		('9871245', 'HP', 'Pavilion 500-210qe', 'Intel i5-4531', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
		('9871256', 'HP', 'Pavilion 500-210qe', 'Intel i5-4532', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
		('9871267', 'HP', 'Pavilion 500-210qe', 'Intel i5-4533', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
		('9871278', 'HP', 'Pavilion 500-210qe', 'Intel i5-4534', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
		('9871289', 'HP', 'Pavilion 500-210qe', 'Intel i5-4535', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
		('6541001 ', 'Dell', 'OptiPlex 9020 ', 'Intel i7-4770', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
        ('6541002 ', 'Dell', 'OptiPlex 9021 ', 'Intel i7-4771', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
        ('6541003 ', 'Dell', 'OptiPlex 9022 ', 'Intel i7-4772', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
		('6541004 ', 'Dell', 'OptiPlex 9023 ', 'Intel i7-4773', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
		('6541005 ', 'Dell', 'OptiPlex 9024 ', 'Intel i7-4774', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
		('6541006 ', 'Dell', 'OptiPlex 9025 ', 'Intel i7-4775', 3.00, '8.0 Gbytes', '1.0 Tbytes');

select*from abc_computer.computer_table;

select*from abc_computer.computer_table where Make= 'HP';
select*from abc_computer.computer_table where Make= 'Dell';

alter table abc_computer.computer_table add Graphics varchar(40);

update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '9871234';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '9871245';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '9871256';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '9871267';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '9871278';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '9871289';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '6541001';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '6541002';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '6541003';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '6541004';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '6541005';
update abc_computer.computer_table set Graphics = 'Integrated Intel HD Graphics 4600' where SerialNumber = '6541006';

alter table abc_computer.computer_table drop column ProcessorSpeed;

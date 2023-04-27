create database customer;
create table customer.tblcustomer
(CustomerID int not null primary key, 
CustomerName varchar(40) not null,
Municipality varchar(40) not null, 
City varchar(40) not null, SalaryInPeso int not null);

insert into customer.tblcustomer ( CustomerID, CustomerName, Municipality, City, SalaryInPeso)
values 
(1, 'Gina de Lean', 'Apalit', 'Pampanga', 5000),
(2, 'Amara Luna', 'Mexico', 'Pampanga', 6000),
(3, 'Lucila Maulon','Angat','Bulacan', 1000),
(4, 'Rafael Santos','Lumban','Laguna',4500),
(5, 'Maricel Moran','Calumpit','Bulacan', 12000),
(6, 'Antonio Moreno', 'Santa Maria','Bulacan', 8500),
(7, 'Harra Moos','Alaminos','Laguna',6000),
(8, 'Fred Gregorio','Lumban','Laguna',5000),
(9, 'Maria Andres','Porac','Pampanga',1800),
(10, 'Liza Ramos',' Alaminos','Laguna',14000);


-- selects all records form pampanga --
select*from customer.tblcustomer where city = 'Pampanga';

-- selects all records from porac and pampanga --
select*from customer.tblcustomer where municipality = 'Porac' and city = 'Pampanga';

-- selects records from  either Apalit or Angat --
select*from customer.tblcustomer where municipality = 'Apalit' or municipality = 'Angat';

-- selects all records from Apalit or Angat --
select*from customer.tblcustomer where not city = 'Pampanga';

-- customer with the minimum salary and max salary--
select min(SalaryInPeso)
from customer.tblcustomer;

select max(SalaryInPeso)
from customer.tblcustomer;

-- csutomer with max salary with condition --
select max(SalaryInPeso)
from customer.tblcustomer
where city = 'Pampanga';

-- customer by order ascending and descending --
select*from customer.tblcustomer order by city asc;
select*from customer.tblcustomer order by city desc;

select*from customer.tblcustomer order by city asc, CustomerName asc;


select*from customer.tblcustomer;
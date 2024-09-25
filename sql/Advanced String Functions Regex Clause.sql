-- 1667. Fix Names in a Table

select user_id, concat(upper(substr(name, 1, 1)), lower(substr(name, 2))) as name
from users
order by user_id

-- substr(str, startpos (starts at 1), len)

-- 1527. Patients With a Condition

select patient_id, patient_name, conditions
from patients
where conditions REGEXP "^DIAB1| DIAB1"

-- REGEXP!

-- 196. Delete Duplicate Emails

-- DELETE FROM table_name WHERE condition;
-- INSERT INTO table_name VALUES (value1, value2, value3, ...);
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);

WITH min_ids AS (
    SELECT MIN(id) AS id
    FROM person
    GROUP BY email
)
DELETE FROM person
WHERE id NOT IN (SELECT id FROM min_ids);
-- using cte's
-- can also do with joins
delete p1 
from Person p1
join Person p2
on p1.email = p2.email
where p1.id > p2.id

-- 176. Second Highest Salary

select max(salary) as SecondHighestSalary from (
    select salary,
    dense_rank() over(order by salary desc) salary_rank
    from employee
    group by salary
    order by salary desc
    limit 2
) t1
where salary_rank = 2
-- max or min will return null

--simpler
select max(salary) as SecondHighestSalary from employee
where salary < (select max(salary) from employee)

-- or even better
select (
select Salary
from Employee
group by salary
order by salary desc
limit 1
offset 1
) as SecondHighestSalary
-- using offset, but has to be?

-- 1484. Group Sold Products By The Date
select sell_date, count(distinct product) as num_sold, 
group_concat(distinct product order by product asc separator ',') as products
from activities
group by sell_date
order by sell_date
-- group_concat(col order by col asc separator ',') as col

-- 1327. List the Products Ordered in a Period
select p.product_name, sum(unit) as unit from Orders o
join Products p
on o.product_id = p.product_id
where o.order_date >= '2020-02-01' and o.order_date <= '2020-02-29'
group by p.product_name
having sum(unit) >= 100

select p.product_name, sum(unit) as unit from Orders o
join Products p
on o.product_id = p.product_id
WHERE YEAR(o.order_date)='2020' AND MONTH(o.order_date)='02'
group by p.product_name
having sum(unit) >= 100
-- Year(date) and Month(date)

-- 1517. Find Users With Valid E-Mails
SELECT user_id, name, mail 
FROM Users
where  mail REGEXP '^([a-zA-Z])([a-zA-Z0-9._-]*)@leetcode\\.com$';
-- regexp!

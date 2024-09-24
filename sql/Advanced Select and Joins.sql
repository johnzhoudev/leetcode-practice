--- 1731. The Number of Employees Which Report to Each Employee

select 
    e1.employee_id, 
    e1.name, 
    count(distinct e2.employee_id) as reports_count,
    round(avg(e2.age), 0) as average_age    
from Employees e1
join Employees e2
on e1.employee_id = e2.reports_to
group by e1.employee_id, e1.name
order by e1.employee_id 

-- 1789. Primary Department for Each Employee

select employee_id, department_id from Employee
where primary_flag = "Y" or employee_id in
(select employee_id from Employee group by employee_id having count(distinct department_id) = 1)

SELECT employee_id, department_id 
FROM Employee
WHERE primary_flag = 'Y'
UNION
SELECT employee_id, department_id 
FROM Employee 
GROUP BY employee_id
HAVING COUNT(employee_id) = 1
-- OR, use union!

-- 610. Triangle Judgement

SELECT x, y, z
FROM Triangle t
WHERE (x + y > z) AND (x + z > y) AND (y + z > x);

SELECT x, y, z, (case when (x + y > z) AND (x + z > y) AND (y + z > x) then 'Yes' else 'No' end) as triangle
FROM Triangle t;

-- 180. Consecutive Numbers
select distinct l1.num as ConsecutiveNums from Logs l1
join Logs l2
on l1.num = l2.num and l1.id = l2.id + 1
join Logs l3
on l2.num = l3.num and l2.id = l3.id + 1

SELECT distinct 
    i1.num as ConsecutiveNums 
FROM 
    logs i1,
    logs i2,
    logs i3
WHERE 
    i1.id=i2.id+1 AND 
    i2.id=i3.id+1 AND 
    i1.num=i2.num AND 
    i2.num=i3.num

with cte as (
    select num,
    lead(num,1) over() num1, -- empty partition section!
    lead(num,2) over() num2
    from logs

)
select distinct num ConsecutiveNums from cte where (num=num1) and (num=num2)

-- lots of ways to skin this cat.

-- 1164. Product Price at a Given Date

select product_id, new_price as price from Products p
where (product_id, change_date) in 
(select product_id, max(change_date) from Products where change_date <= '2019-08-16' group by product_id)
union
select product_id, 10 as price from Products group by product_id having min(change_date) > '2019-08-16'

-- union, also example of using where and group by!

-- 1204. Last Person to Fit in the Bus
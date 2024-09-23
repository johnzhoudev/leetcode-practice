-- 2356. Number of Unique Subjects Taught by Each Teacher

select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id;

-- 1141. User Activity for the Past 30 Days I

select activity_date as day, count(distinct user_id) as active_users
from Activity
where date_add(activity_date, interval 30 day) > '2019-07-27' and activity_date <= '2019-07-27'
group by activity_date;

-- tricky date ranges

-- 1070. Product Sales Analysis III

select product_id, year as first_year, quantity, price
from Sales
where (product_id, year) in 
    (select product_id, min(year) from Sales group by product_id);

-- watch out for subquery:
SELECT product_id, sale_id, MIN(year)
FROM Sales
GROUP BY product_id;
-- sql does not guarantee sale_id is gonna be the right one.

-- 596. Classes More Than 5 Students

select class from Courses group by class having count(distinct student) >= 5

-- group by must be before having!

-- 1729. Find Followers Count
select user_id, count(distinct follower_id) as followers_count from Followers group by user_id order by user_id asc;

-- 619. Biggest Single Number
select max(num) as num from 
    (select num from MyNumbers
        group by num
        having count(num) = 1) as t2
-- subquery!


-- 1045. Customers Who Bought All Products
select customer_id from Customer c
group by customer_id
having count(distinct product_key) = (select count(*) from Product)
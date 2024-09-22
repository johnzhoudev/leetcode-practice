-- 1251. Average Selling Price

select p.product_id, coalesce(round(SUM(price * units) / sum(units), 2), 0) as average_price from Prices p
left join UnitsSold u
on u.product_id = p.product_id and p.start_date <= u.purchase_date and u.purchase_date <= p.end_date
group by p.product_id;

-- compare dates with <=, also avg and sum return null instead of 0


--- 1075. Project Employees I
select project_id, round(avg(experience_years), 2) as average_years from Project p
join Employee e
on p.employee_id = e.employee_id
group by project_id;

-- join is fine, since each project will have employees

--- 1633. Percentage of Users Attended a Contest
select contest_id, round(count(distinct user_id) * 100 / (select count(*) from Users), 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id asc;

-- Scalar subquery

-- 1211. Queries Quality and Percentage
select query_name, 
    round(avg(rating / position), 2) as quality,
    round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(rating), 2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name;

-- case when cond then res1 else res2 end

-- 1193. Monthly Transactions I

select 
    DATE_FORMAT(trans_date, '%Y-%m') as month, 
    country, 
    count(distinct id) as trans_count,
    count(distinct case when state = 'approved' then id end) as approved_count,
    sum(amount) as trans_total_amount,
    sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions
group by month, country;

-- Careful with sum, could be null so specify 0
-- distinct when it makes sense!

-- 1174. Immediate Food Delivery II

select round(avg(case when d1.order_date = d1.customer_pref_delivery_date then 1 else 0 end) * 100, 2) as immediate_percentage
from Delivery d1
left join Delivery d2
on d1.customer_id = d2.customer_id and d2.order_date < d1.order_date
where d2.order_date is null;

-- Better:

select round(avg(d1.order_date = d1.customer_pref_delivery_date) * 100, 2) as immediate_percentage
from Delivery d1
where (d1.customer_id, d1.order_date) in
(select customer_id, min(order_date) from Delivery group by customer_id);

-- Use where (a, b) in subquery
-- also clever order1 = order2 produces boolean 1 0 value

-- 550. Game Play Analysis IV

select round(avg(case when a2.event_date is null then 0 else 1 end), 2) as fraction
from Activity a1
left join Activity a2
on a1.player_id = a2.player_id and a2.event_date = date_add(a1.event_date, interval 1 day)
where (a1.player_id, a1.event_date) in
(select player_id, min(event_date) from Activity group by player_id)

-- Better

select round(count(a.player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from Activity a
where (a.player_id, date_sub(a.event_date, interval 1 day))
in (select player_id, min(event_date) from Activity group by player_id)

-- no need for join, just use where clause where date_sub in first dates
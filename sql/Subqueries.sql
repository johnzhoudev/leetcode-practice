-- 1978. Employees Whose Manager Left the Company

select employee_id from Employees
where salary < 30000 and manager_id not in (select employee_id from employees)
order by employee_id

-- subquery

-- 626. Exchange Seats!

select s1.id as id, coalesce(s2.student, s1.student) as student from Seat s1
left join Seat s2
on s1.id + 1 = s2.id
where (s1.id % 2) = 1
union
select s1.id as id, s2.student from Seat s1
join Seat s2
on s1.id = s2.id + 1
where (s1.id % 2) = 0
order by id asc

-- 1341. Movie Rating

(select name as results from Users u
join MovieRating mr
on mr.user_id = u.user_id
group by u.user_id
order by count(distinct mr.movie_id) desc, name asc
limit 1)
union all
(select title as results from Movies m
join MovieRating mr
on m.movie_id = mr.movie_id 
where mr.created_at >= '2020-02-01' and mr.created_at <= '2020-02-29'
group by m.movie_id
order by avg(mr.rating) desc, m.title asc
limit 1)

-- Good example of ordering by an aggregate!

-- 1321. Restaurant Growth

with cte as (
select visited_on, 
    sum(amount) over(order by visited_on range interval 6 day preceding) amount,
    round(avg(amount) over(order by visited_on range interval 6 day preceding), 2) as average_amount
from Customer
)
select distinct visited_on, amount, round(amount / 7, 2) as average_amount from cte
where visited_on >= date_add((select min(visited_on) from Customer), interval 6 day)
-- avg doesn't work here bc we need to divide by 7, and if there are rpt entries on day 10 then we divide by 8 in avg

with cte as (
select visited_on, 
    sum(amount) over(order by visited_on range interval 6 day preceding) amount,
    dense_rank() over(order by visited_on) day
from Customer
)
select distinct visited_on, amount, round(amount / 7, 2) as average_amount from cte
where day >= 7

-- Pro tip: dense_rank() ranks each field 1 2 3..., for dupes same rank, but next doesn't skip.

-- 602. Friend Requests II: Who Has the Most Friends

with incoming as 
(select accepter_id as id, count(distinct requester_id) as num from RequestAccepted
group by accepter_id),

outgoing as 
(select requester_id as id, count(distinct accepter_id) as num from RequestAccepted
group by requester_id),

res as (
select coalesce(i.id, o.id) as id, coalesce(i.num, 0) + coalesce(o.num, 0) as num from incoming i
left join outgoing o
on i.id = o.id
union -- removes duplicates
select coalesce(i.id, o.id) as id, coalesce(i.num, 0) + coalesce(o.num, 0) as num from incoming i
right join outgoing o
on i.id = o.id)

select id, num from res
group by id
order by num desc
limit 1

-- too complicated, just do union all!
select id1 as id, count(id2) as num from
(select requester_id as id1, accepter_id as id2 from RequestAccepted
union
select accepter_id as id1, requester_id as id2 from RequestAccepted) as tb1
group by id1
order by count(id2) desc
limit 1

-- Lesson here: requester accepter union all, also coalescing values and full join example


-- 585. Investments in 2016
with validpids as (
    select distinct i.pid from Insurance i
    join insurance i2
    on i.tiv_2015 = i2.tiv_2015 and i.pid != i2.pid
),
validlatlon as (
    select lat, lon
    from insurance
    group by lat, lon
    having count(pid) = 1
)
select round(sum(tiv_2016), 2) as tiv_2016
from insurance
where pid in (select * from validpids) and (lat, lon) in (select * from validlatlon)

-- Better: use group by and count!
select round(sum(tiv_2016), 2) as tiv_2016 from insurance
where tiv_2015 in (
    select tiv_2015 from insurance
    group by tiv_2015
    having count(tiv_2015) > 1 
) and (lat, lon) in (
    select lat, lon from insurance
    group by lat, lon
    having count(pid) = 1
)

-- 185. Department Top Three Salaries

with cte as (select d.name as Department, e.name, e.salary,
dense_rank() over(partition by e.departmentId order by e.salary desc) salary_rank
from employee e
join department d
on d.id = e.departmentId)
select department, name as Employee, salary as Salary from cte
where salary_rank <= 3

-- dense_rank() ftw
-- Getting top or bottom 3 things using dense rank!


select d.name as Department, e.name as Employee, e.Salary as Salary from Employee e
join Department d
on d.id = e.departmentId
where 3 > (
    select count(distinct e2.salary) from Employee e2
    where e2.salary > e.Salary and e2.departmentId = e.departmentId
)

-- Can incorporate current row values into subquery in where clause!!!
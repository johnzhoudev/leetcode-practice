select s.user_id, 
    round(coalesce(count(case when c.action = 'confirmed' then 1 end) / count(c.user_id), 0), 2) as confirmation_rate
from Signups s
left join Confirmations c
on c.user_id = s.user_id
group by s.user_id;

select s.user_id, round(avg(if(action='confirmed', 1, 0)), 2) as confirmation_rate from Signups s
left join Confirmations c
on c.user_id = s.user_id
group by s.user_id;

-- case when cond then 1 when then else
-- coalesce
-- or, mysql use if(cond, true, false)
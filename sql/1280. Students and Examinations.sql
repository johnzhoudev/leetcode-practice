select stu.student_id, student_name, sub.subject_name, count(e.subject_name) as attended_exams
from Students stu
join Subjects sub
left join Examinations e
on e.student_id = stu.student_id and e.subject_name = sub.subject_name
group by stu.student_id, sub.subject_name
order by stu.student_id ASC, sub.subject_name ASC;
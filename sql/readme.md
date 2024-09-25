
# SQL Cheat Sheet

https://leetcode.com/studyplan/top-sql-50/

## Selects
- != doesn't account for NULL - see 584, 577
- select asdf as jkl - for output labelling!
- CHAR_LENGTH - number of chars of a string, LENGTH - bytes of a string - 1683

## Joins
- Left join to find values null if not exist - 1581
- DATE_SUB / DATE_ADD(date, interval 1 day) - 197
- round(item, 2)
- start and end timestamps - 1661

- count(*) counts nulls, count(col) does not count nulls! - 1280
- group by and having count() - 570
- case when cond then 1 when then else, coalesce or mysql use if(cond, true, false) - 1934

## Selects
- % operator, 620
- Comparing dates with <>=, 1251
- Scalar subquery, 1633
- where (a, b) in (subquery), min(date) - 1174, 550
- date sub - 550

## Sorting and Grouping
- queries with aggregates, aggregate func, rest must be in group by - 1070
- group by before having clause - 596

## Advanced Selects
- unions! 1789, 1907
- cumulative window functions sum over order by 1204
- where clause, and group by where filters out - 1164
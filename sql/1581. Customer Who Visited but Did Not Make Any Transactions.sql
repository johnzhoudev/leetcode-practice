# Write your MySQL query statement below
SELECT customer_id, COUNT(v.visit_id) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
where t.transaction_id is NULL
GROUP BY customer_id;
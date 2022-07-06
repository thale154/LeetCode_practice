# Write your MySQL query statement below
SELECT
    customer_id,
    COUNT(v.visit_id) as count_no_trans
FROM
    Visits as v
    NATURAL LEFT JOIN Transactions as t
WHERE
    t.visit_id IS NULL
GROUP BY customer_id
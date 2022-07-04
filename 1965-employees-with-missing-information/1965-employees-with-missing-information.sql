# Write your MySQL query statement below
SELECT
    employee_id
FROM (
    Employees as e
    LEFT JOIN Salaries as s
    USING(employee_id)
)
WHERE s.salary IS NULL
UNION
SELECT
    employee_id
FROM (
    Employees as e
    RIGHT JOIN Salaries as s
    USING(employee_id)
)
WHERE e.name IS NULL
ORDER BY 1;
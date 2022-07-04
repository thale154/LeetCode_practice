# Write your MySQL query statement below
SELECT 
    id,
    CASE
        WHEN p_id is null then 'Root'
        WHEN id in (SELECT p_id FROM Tree) then 'Inner'
        ELSE 'Leaf'
    END as type
FROM
    Tree
ORDER By id;
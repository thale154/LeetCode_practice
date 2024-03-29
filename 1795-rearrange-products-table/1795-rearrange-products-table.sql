# Write your MySQL query statement below
SELECT * 
FROM 
(
    SELECT product_id, 'store1' as store, store1 as price FROM Products
    UNION 
    SELECT product_id, 'store2' as store, store2 as price FROM Products
    UNION
    SELECT product_id, 'store3' as store, store3 as price FROM Products
) as sub
WHERE price IS NOT NULL
ORDER BY 1,2;


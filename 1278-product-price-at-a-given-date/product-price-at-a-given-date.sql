# Write your MySQL query statement below


WITH Temp  AS
(SELECT * , ROW_NUMBER() OVER(PARTITION BY product_id  ORDER BY change_date DESC) as rn
FROM Products
WHERE change_date <= '2019-08-16')

SELECT t.product_id , t.new_price as price
FROM Temp t
WHERE rn = 1

UNION 


SELECT p.product_id, 10 as price
FROM Products p
LEFT JOIN Temp t
ON p.product_id = t.product_id
WHERE t.product_id IS NULL;


-- SELECT *
-- FROM Temp
# Write your MySQL query statement below

WITH temp AS 
(SELECT d.name AS Department , e.name AS Employee , salary AS Salary,
DENSE_RANK() OVER(PARTITION BY departmentId  ORDER BY salary DESC) as rn
FROM Employee e JOIN Department d
ON e.departmentId = d.id)

SELECT Department , Employee , Salary
FROM temp 
WHERE rn <= 3

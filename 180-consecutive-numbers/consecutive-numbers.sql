# Write your MySQL query statement below

 
WITH TEMP AS (
    SELECT * , ROW_NUMBER() OVER(PARTITION BY num ORDER  BY id ) as rn
    FROM Logs
    

), 

grp AS (
    SELECT * , id - rn AS diff
    FROM TEMP

)

SELECT DISTINCT num AS ConsecutiveNums
FROM grp
GROUP BY num ,diff
HAVING COUNT(*) >= 3
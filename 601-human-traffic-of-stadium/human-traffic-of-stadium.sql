# Write your MySQL query statement below

WITH temp AS (
    SELECT * , ROW_NUMBER() OVER( ORDER BY visit_date) as rn 
    FROM Stadium 
    WHERE people >= 100
    
    ),

    grp as (
    SELECT * , id - rn AS diff
    FROM temp
    )
    

SELECT  id , visit_date , people
FROM grp
WHERE diff in (SELECT diff
                FROM  grp 
                GROUP BY diff
                HAVING COUNT(*) >= 3)








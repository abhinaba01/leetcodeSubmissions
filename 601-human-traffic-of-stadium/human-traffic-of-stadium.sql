WITH TEMP AS (
    SELECT * , ROW_NUMBER() OVER(ORDER BY visit_date) as rn 
    FROM Stadium
    WHERE people >= 100

)
,

grp AS (
SELECT * ,t.id - t.rn as diff
FROM TEMP t
    
)

SELECT  id , visit_date , people
FROM grp 
WHERE diff IN (
    SELECT diff
    FROM grp
    GROUP BY diff
    HAVING COUNT(*) >= 3
)







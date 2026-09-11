WITH RankedEmployees AS (
    SELECT Department.name as Department, 
           Employee.name as Employee , 
           Employee.salary as Salary,
           DENSE_RANK() OVER(PARTITION BY Employee.departmentId ORDER BY Employee.salary DESC) AS SalaryRank
    FROM Employee 
    JOIN Department ON Employee.departmentId = Department.id
    )

SELECT Department , Employee , Salary
FROM RankedEmployees 
WHERE SalaryRank <= 3

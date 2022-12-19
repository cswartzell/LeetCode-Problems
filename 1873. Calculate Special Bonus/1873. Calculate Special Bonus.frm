# 12-18-2022 Leetcode 1873. Calculate Special Bonus
# https://leetcode.com/problems/calculate-special-bonus/


#I think ive decided I HATE mysql syntax. Its so... off

# Write your MySQL query statement below
#The explore card has NOT gone over nearly enough to
#accomplish this. It hasnt said how to use default values,
#or how to sort, or how to do math within a compare

SELECT employee_id, CASE WHEN (employee_id %2=1 AND name NOT LIKE('M%')) THEN salary 
ELSE 0 END AS bonus FROM Employees ORDER BY employee_id
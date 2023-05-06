# 12-18-2022 Leetcode 627. Swap Salary
# https://leetcode.com/problems/swap-salary/description/

# Write your MySQL query statement below
# UPDATE salary 
# SET 
#     sex = CASE 
#         WHEN ( sex = 'm') THEN 'f' 
#         ELSE 'm' 
#     END;
    
    update salary set sex = IF (sex = "m", "f", "m");


# UPDATE salary
# SET
#     sex = CASE sex
#         WHEN 'm' THEN 'f'
#         ELSE 'm'
#     END;
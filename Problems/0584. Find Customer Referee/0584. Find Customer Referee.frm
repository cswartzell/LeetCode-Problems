# 12-18-2022 Leetcode 584. Find Customer Referee
#  https://leetcode.com/problems/find-customer-referee/

#Straightforward

# Write your MySQL query statement below
SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL;
accounts = [[1, 2, 3, 5], [3, 2, 1]]

print(max(sum(x) for x in accounts))


# Problem states at least one account per customer, with acocounts strictly > 0


# for custumer_row in range(len(accounts)):
#     tmp_sum = 0
#     for account_elm in range(len(accounts[custumer_row])):
#         tmp_sum += accounts[custumer_row][account_elm]
#     if tmp_sum > richest_customer_wealth:
#         richest_customer_wealth = tmp_sum

# # return richest_customer_wealth
# print(richest_customer_wealth)

# https://leetcode.com/problems/nth-digit/

# [1, 9] has 9 * 10**0 numbers, [10-99] has 9 * 10**1, [100, 999] has 9 * 10**2
#  1 2 3 4 ... 9  | 10 11 12 ... 99  | 100 .... 999
#        9                  90              900

# For example we're looking for 100th digits
# 1000 - 9 * 10**0 - 9 * 10**1 = 811 th digit sit inside [100, 999]
# 811 // 3 = 270 since (each number has 3 digits in this range) so 
# 270 means 270th number after 100 -> means the number we're looking for is 370
# 

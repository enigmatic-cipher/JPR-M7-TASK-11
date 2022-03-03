"""
Given a number n as input, count the number of times the digit 5 appears in the number. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> 234561
Output-> 1
"""

def countFive(num):
  num1 = str(num)
  count = 0
  e = num1[0]
  if (e=='5'):
    count = count + 1
  return count + countFive(num1[1:])

num = 234561
print(countFive(num))

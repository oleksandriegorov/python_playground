# Found reference at https://www.youtube.com/watch?v=JaosdXkUWTs
from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) == 0 or max(prices) == 0:
      return 0
    if sorted(prices, reverse=True) == prices:
      return 0
    day = 0
    profit = 0
    lmin = 0
    lmax = 0
    buy=True
    while day < len(prices)-1:
      if prices[day + 1] >= prices[day] and buy:
        lmin=prices[day]
        buy=False
      elif prices[day + 1] <= prices[day] and not buy:
        lmax=prices[day]
        profit+=lmax-lmin
        lmax=lmin=0
        buy=True
      day+=1
    if not buy and prices[day] >= lmin:
      profit+=prices[day] - lmin
    return profit


a=Solution()
print(a.maxProfit([0,1,1,1,1]))
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price,sell_price = prices[0],prices[0]
        max_profit = 0

        for elem in prices:
            if elem < buy_price:
                buy_price = elem
            else:
                sell_price = elem
                max_profit = max(max_profit, sell_price - buy_price)

        return max_profit
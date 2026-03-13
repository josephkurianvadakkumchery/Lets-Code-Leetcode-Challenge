class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        l1=prices.pop(prices.index(min(prices)))
        l2=prices.pop(prices.index(min(prices)))
        if((l1+l2)<=money):
            return (money-(l1+l2))
        else:
            return money

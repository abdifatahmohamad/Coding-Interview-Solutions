class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = float("-Inf")
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            richest = max(richest, wealth)
        return richest
        
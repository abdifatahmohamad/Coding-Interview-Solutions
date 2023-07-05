class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = float("-Inf")
        wealth = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
            richest = max(richest, wealth)
            wealth = 0
        return richest
        
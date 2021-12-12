class Solution:
    def kth_factor(self, n, k):
        return self.keth_factor_helper(n, k, 1)

    def keth_factor_helper(self, n, k, counter):
        # Base case:
        if k == 0:
            return counter - 1
        # Another case:
        if counter > n:
            return - 1

        # Recursion case:
        return self.keth_factor_helper(n, k - 1 if n % counter == 0 else k, counter + 1)


solution = Solution()

print(solution.kth_factor(20, 3))  # Output is 4

# Let's say the input is n = 20 and k = 3.
# 10 has a factor of 1, 2, 4, 5, 10.
# So you need to return the 3rd factor
# in this case k = 3. So the output is 4.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Not going to be an anagram if length of p > length s
        if len(p) > len(s):
            return []

        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1

        # Compare two hashmaps, if they are equal assign the result to list with zero inserted
        res = [0] if pCount == sCount else []
        l = 0
        for r in range(len(p), len(s)):
            # Add character at index r to our hash map
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            # Remove the character that was at left index
            sCount[s[l]] -= 1

            # If count of character at left index becomes zero, remove/pop off from hashmap
            if sCount[s[l]] == 0:
                # Pop off that value from hashmap
                sCount.pop(s[l])
            # Increment left pointer
            l += 1

            # If two hashmaps are equal, append left index to the result
            if sCount == pCount:
                res.append(l)
        return res
        
#User function Template for python3
from collections import defaultdict
class Solution:
    def sumOfDependencies(self,adj,V):
        adjacency = defaultdict(list)
        # for edge in adj:
        #     print(edge)
        
        res = 0
        for edge in adj:
            res += len(edge)

        return res
            
        
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[[] for i in range(N)]
        s=list(map(int,input().strip().split()))
        for i in range(0,2*M,2):
            x=s[i]
            y=s[i+1]
            a[x].append(y)
        ob=Solution()
        print(ob.sumOfDependencies(a,N))
        


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = [0] * V
        res = []
        stack = [0]  # Start the DFS traversal from node 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = 1
                res.append(node)
                # Add the neighbors of the node to the stack
                stack.extend(reversed(adj[node]))
        return res
                
                
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends
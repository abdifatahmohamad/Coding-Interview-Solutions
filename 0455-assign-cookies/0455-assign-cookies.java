class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int maxContent = 0;
        Arrays.sort(g);
        Arrays.sort(s);
        int i = 0;
        int j = 0; // cooky
        while(i <= g.length -1 && j <= s.length -1){
            if(s[j] >= g[i]){
                maxContent++;
                i++;
            }
            j++;
        } 
        
        return maxContent;
    }
}
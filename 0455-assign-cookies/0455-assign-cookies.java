class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int maxContent = 0;
        Arrays.sort(g);
        Arrays.sort(s);
        int i = g.length -1;
        int j = s.length -1; // cooky
        while(i >= 0 && j >= 0){
            if(s[j] >= g[i]){
                maxContent++;
                i--;
                j--;
            }else{
                i--;
            }
        } 
        
        return maxContent;
    }
}
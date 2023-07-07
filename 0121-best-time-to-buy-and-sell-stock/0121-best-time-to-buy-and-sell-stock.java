class Solution {
    public int maxProfit(int[] prices) {      
        int maxProfit = 0;
        int left = 0;
        int right = 1;
        while(right < prices.length){     
            if(prices[left] < prices[right]){
                int profit = Math.abs(prices[right] -  prices[left]);
                maxProfit = Math.max(maxProfit, profit);
            } else{
                // low price
                left = right;
            }
            
            right ++;
            
        }
        
        
        
        return maxProfit;
        
    }
}
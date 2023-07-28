class Solution {
    Map<Character, Integer> map;
    public int canBeTypedWords(String text, String brokenLetters) {
        map = new HashMap<>();
        for(char c : brokenLetters.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        int res = 0;
        for(String word : text.split(" ")){
            if(canBeFullyTyped(word)){
                res++;
            }  
        }
        return res;
    }
    
    private boolean canBeFullyTyped(String word){
        for(char c : word.toCharArray()){
            if(map.containsKey(c)){
                return false;
            }
        }
        return true;
    }
}
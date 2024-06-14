class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        Map<Character, Integer> map = new HashMap<>();
        for(char c : brokenLetters.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        int res = 0;
        for(String word : text.split(" ")){
            res++;
            for(char c : word.toCharArray()){
                if(map.containsKey(c)){
                    res--;
                    break;
                }
            }           
        }
        return res;
    }
}
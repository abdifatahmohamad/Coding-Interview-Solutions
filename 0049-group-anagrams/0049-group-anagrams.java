class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Created result array or array
        List<List<String>> res = new ArrayList<>();
        // Create map to fasilitate the operations
        Map<String, List<String>> map = new HashMap<>();
        // Loop the give array string
        for(String word : strs){
            // Convert each word into character array
            char[] chars = word.toCharArray();
            // Sort characters
            Arrays.sort(chars);
            // Convert character arrays back to string
            // String sortedStr = new String(chars);
            String sortedStr = String.valueOf(chars);
            // Check if the key already exists in the map
            if(!map.containsKey(sortedStr)){
               // If not, create a new list and put the original string in it
                List<String> newList = new ArrayList<>();
                newList.add(word);
                map.put(sortedStr, newList);
            }else{
             // If the key already exists, add the original string to the existing list
                map.get(sortedStr).add(word);
            }
        }
        // Append map values to the result
        for(List<String> words : map.values()){
            res.add(words);
        }
        return res;
    }
}
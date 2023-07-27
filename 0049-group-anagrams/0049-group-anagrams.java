class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        // Create a map to store sorted strings as keys and their original strings as values
        Map<String, List<String>> map = new HashMap<>();

        // Loop through each string in the array
        for (String word : strs) {
            // Sort the characters of the string and create a sorted key
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);

            // Check if the key already exists in the map
            if (!map.containsKey(sortedStr)) {
                // If not, create a new list and put the original string in it
                List<String> newList = new ArrayList<>();
                newList.add(word);
                map.put(sortedStr, newList);
            } else {
                // If the key already exists, add the original string to the existing list
                map.get(sortedStr).add(word);
            }
        }
        
        // Print map keys and values
//         for(String key : map.keySet()){
//             List<String> values = map.get(key);
//             System.out.println(key + ":" + values);
//         }
        
        for (List<String> words : map.values()) {
            res.add(words);
        } 
        return res;    
    }
}
class Solution {
    public List<Integer> partitionLabels(String s) {
        Map<Character, Integer> map = new HashMap<>();
        char[] chars = s.toCharArray();
        for(int i = 0; i < chars.length; i++){
            map.put(chars[i], i);
        }
            
        List<Integer> res = new ArrayList<>();
        int start = 0; 
        int end = 0;
        int i = 0;
        while (i < s.length()) {
            int lastIndex = map.get(s.charAt(i));
            end = Math.max(end, lastIndex);

            // If the current index is equal to the end index, we have found a partition
            if (i == end) {
                res.add(end - start + 1);
                start = end + 1; // Move the start index to the next partition
            }
            i++;
        }

        return res;
    }
}
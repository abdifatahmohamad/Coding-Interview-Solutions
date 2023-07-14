class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        Map<Integer, List<Integer>> map = new HashMap<>();

        for (int num : nums) {
            boolean added = false;
            for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
                if (!entry.getValue().contains(num)) {
                    // If the current row doesn't contain the number, add it to the row
                    entry.getValue().add(num);
                    added = true;
                    break;
                }
            }
            if (!added) {
                // If no existing row can accommodate the number, create a new row
                List<Integer> newRow = new ArrayList<>();
                newRow.add(num);
                map.put(map.size(), newRow);
            }
        }

        // Convert the map into a list of lists
        List<List<Integer>> res = new ArrayList<>();
        for (List<Integer> list : map.values()) {
            res.add(list);
        }

        return res;
        
    }
}

/*
    nums = [1,3,4,1,2,3,1]
    Output: [
    
            [1,3,4,2],
            [1,3],
            [1]
            
            ]

*/
public class Solution {
    private Map<Character, String> nums;
    private List<String> res;

    public List<String> letterCombinations(String digits) {
        nums = new HashMap<>();
        nums.put('2', "abc");
        nums.put('3', "def");
        nums.put('4', "ghi");
        nums.put('5', "jkl");
        nums.put('6', "mno");
        nums.put('7', "pqrs");
        nums.put('8', "tuv");
        nums.put('9', "wxyz");

        res = new ArrayList<>();

        if (!digits.isEmpty()) {
            backtrack(0, new StringBuilder(), digits);
        }

        return res;
    }

    private void backtrack(int index, StringBuilder current, String digits) {
        if (index == digits.length()) {
            res.add(current.toString());
            return;
        }

        char digit = digits.charAt(index);
        String letters = nums.get(digit);
        for (int i = 0; i < letters.length(); i++) {
            current.append(letters.charAt(i));
            backtrack(index + 1, current, digits);
            current.deleteCharAt(current.length() - 1);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> combinations = solution.letterCombinations("23");
        for (String combination : combinations) {
            System.out.println(combination);
        }
    }
}
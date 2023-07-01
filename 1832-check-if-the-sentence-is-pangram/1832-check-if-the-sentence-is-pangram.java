class Solution {
    public boolean checkIfPangram(String sentence) {
        Set<Character> res = new HashSet<>();
        for (char c : sentence.toCharArray()) {
            res.add(c);
        }
        return res.size() == 26;
    }
}

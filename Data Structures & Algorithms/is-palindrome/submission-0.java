class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll(
                "[^a-zA-Z0-9]", "").toLowerCase();

        for (int i = 0; i < s.length(); i++) {
            char one = s.charAt(i);
            char two = s.charAt(s.length() - (i+1));

            if (one != two) return false;
        }

        return true;
    }
}

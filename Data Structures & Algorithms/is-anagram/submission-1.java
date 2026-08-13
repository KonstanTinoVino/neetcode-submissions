class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        char[] chars = s.toCharArray();
        Arrays.sort(chars);

        char[] chars2 = t.toCharArray();
        Arrays.sort(chars2);

        return new String(chars).equals(new String(chars2));
    }
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int j = 0;

        for (int k = 0; k < nums.length; k++) {
            i = nums[k];
            for (int l = k+1; l < nums.length; l++) {
                j = nums[l];
                if (i + j == target) return new int[]{k, l};
            }
        }
        return null; 
    }
}

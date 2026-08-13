class Solution {

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Check if target is present at mid
            if (nums[mid] == target) {
                return mid;
            }

            // If target is greater, ignore left half
            if (nums[mid] < target) {
                left = mid + 1;
            } 
            // If target is smaller, ignore right half
            else {
                right = mid - 1;
            }
        }

        // Target is not present in array
        return -1;
    }
}

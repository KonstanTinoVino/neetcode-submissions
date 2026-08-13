class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> mySet = Arrays.stream(nums)
        .boxed()
        .collect(Collectors.toCollection(HashSet::new));

        return nums.length > mySet.size();
    }
}

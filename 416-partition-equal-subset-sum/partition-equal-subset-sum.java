class Solution {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int num : nums) total += num;
        if (total % 2 != 0) return false;

        int target = total / 2;
        Set<Integer> possibleSums = new HashSet<>();
        possibleSums.add(0);

        for (int num : nums) {
            Set<Integer> newSums = new HashSet<>();
            for (int s : possibleSums) {
                int newSum = s + num;
                if (newSum == target) return true;
                if (newSum < target) newSums.add(newSum);
            }
            possibleSums.addAll(newSums);
        }
        return possibleSums.contains(target);
    }
        
    
}
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n==1){
            return nums[0];
        } 
        if(n==2){
            return Math.max(nums[0],nums[1]);
        } 
        int l[] = new int[n];  
        l[0] = nums[0]; 
        l[1] = Math.max(nums[0], nums[1]);  
        for(int i=2;i<n;i++){
            l[i] = Math.max(l[i-1],(nums[i]+l[i-2]));
        }
        return l[n-1];
        
    }
}
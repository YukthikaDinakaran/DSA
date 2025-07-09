class Solution {
    public int majorityElement(int[] nums) {
        int count =0;
        int maj =0;
        for(int i=0; i<nums.length;i++){
           if(count == 0){
            count = 1;
            maj = nums[i];
           }else if(maj == nums[i]){
            count++;
           }else{
            count--;
           }
        }
        int cnt = 0;
        for(int i=0; i<nums.length;i++){
            if(nums[i] == maj){
                cnt++;
            }
            if(cnt > ((nums.length)/2)){
                return maj;
            }
            
        }
        return maj;      
    }
}
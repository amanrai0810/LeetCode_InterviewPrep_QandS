class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int diff = Integer.MAX_VALUE;
        int closet=0;
        Arrays.sort(nums);

        for(int i=0; i<nums.length;i++){
             int left = i+1;
        int right = nums.length-1;
            while(left<right){
                int sum = nums[i]+nums[left]+nums[right];
                if(sum==target)return sum;
                if(Math.abs(sum-target)<diff){
                    diff= Math.abs(sum-target);
                    closet=sum;
                }
                if(sum<target){
                    left++;
                }
             else{
                right--;
            }

        }
        }
       
       return closet;
    }
}
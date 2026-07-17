

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        Set<Integer> set1 = new HashSet<>();
        Set<Integer> result = new HashSet<>();

        // Step 1: nums1 ke elements store karo
        for(int num : nums1){
            set1.add(num);
        }

        // Step 2: nums2 check karo
        for(int num : nums2){
            if(set1.contains(num)){
                result.add(num); // duplicate automatically avoid
            }
        }

        // Step 3: set ko array me convert karo
        int[] ans = new int[result.size()];
        int i = 0;

        for(int num : result){
            ans[i++] = num;
        }

        return ans;
    }
}
class Solution {
    public int[] twoSum(int[] nums, int target) {

        int n = nums.length;
        HashMap<Integer , Integer> pos = new HashMap<>();
        int ans[] = new int[2];
        for (int i = 0; i < n; i ++){
            pos.put(nums[i] , i);
        

        }

        for (int i = 0 ; i < n ; i ++){
            int rem = target - nums[i];
            ans[0] = i;
            int idx = pos.getOrDefault(rem , -1);
            
            if((idx != -1) && (idx != i)){
                ans[1] = idx;
                return ans;
            }
            
                
        }

        return ans;
        
        
    }
}
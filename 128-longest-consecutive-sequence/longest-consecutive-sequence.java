class Solution {
    public int longestConsecutive(int[] nums) {

        int n = nums.length;
        if (n == 0){
            return 0;
        }

        HashSet<Integer> set = new HashSet<>();
        int ans = 1;

        for(int i = 0 ; i < n ; i ++){
            set.add(nums[i]);
            
        }

        for(int num:set){
            if (!set.contains(num - 1)){
                int curr = num;
                int len = 1;

                while(set.contains(curr + 1)){
                    curr = curr + 1;
                    len += 1;
                }

                ans = Math.max(len , ans);


            }

        }

        
        return ans;
    }
}
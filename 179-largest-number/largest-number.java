class Solution {
    public String largestNumber(int[] nums) {

        int n = nums.length;
        String[] numStrings = new String[n];

        for(int i = 0 ; i < n ; i ++){
            numStrings[i] = String.valueOf(nums[i]);
        }

       
        Arrays.sort(numStrings , (a,b) -> (b + a).compareTo(a + b));

        if (numStrings[0].equals("0")){
            return "0";
        }
        

        String ans = "";
        for(String numStr:numStrings){
            ans += numStr;
        }

        return ans;

        
    }
}
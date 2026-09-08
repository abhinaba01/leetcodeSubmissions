class Solution {
    

    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String , List<String>> freq = new HashMap<>();

        for(String s:strs){

            char[] chars = s.toCharArray();
            Arrays.sort(chars);

            String k = new String(chars);

            
            freq.computeIfAbsent(k, key -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(freq.values());
        
    }
}
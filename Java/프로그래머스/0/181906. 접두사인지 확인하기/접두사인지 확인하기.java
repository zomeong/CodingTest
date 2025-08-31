class Solution {
    public int solution(String my_string, String is_prefix) {
        int len = is_prefix.length();
        if(len > my_string.length()){
            return 0;
        }
        
        String prefix = my_string.substring(0, len);
        if(prefix.equals(is_prefix)){
            return 1;
        }
        return 0;
    }
}
class Solution {
    public String solution(String rsp) {
        String answer = "";
        
        int len = rsp.length();
        for (int i = 0; i < len; i++){
            char c = rsp.charAt(i);
            
            if(c == '2') answer += "0";
            else if (c == '0') answer += "5";
            else answer += "2";
        }
        
        return answer;
    }
}
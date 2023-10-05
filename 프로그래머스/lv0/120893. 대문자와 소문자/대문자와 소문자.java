import java.util.*;

class Solution {
    public String solution(String str) {
        String answer = "";
        
        for (int i = 0; i < str.length(); i++){
            char ch = str.charAt(i);
            int unicode = (int) ch;
            if(unicode < 91) ch = Character.toLowerCase(ch);
            else ch = Character.toUpperCase(ch);
            answer += ch;
        }
        
        return answer;
    }
}
import java.util.Arrays;

class Solution {
    public long solution(long n) {        
        String l = "" + n;
        long arr[] = new long[l.length()];
        for (int i = 0; i < l.length(); i++){
            arr[i] = n % 10;
            n /= 10;
        }
                    
        Arrays.sort(arr);
        long answer = 0;
        for (int i = 0; i < l.length(); i++){
            answer += arr[i] * Math.pow(10, i);
        }
        return answer;
    }
}
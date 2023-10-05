import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int solution(int num, int k) {
        int answer = 0;
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        // arr에 num을 한자리씩 분리하여 저장
        while(num != 0){
            int s = num % 10;
            num /= 10;
            arr.add(s);
        }
        Collections.reverse(arr);
        
        // k가 있는지 확인
        for(int i = 0; i < arr.size(); i++){
            if (arr.get(i) == k) {
                answer = i + 1;
                break;
            }
            else if (i == arr.size() - 1) answer = -1;
        }
        
        return answer;
    }
}
import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0, c = 0;
        boolean exist[] = new boolean[10];
        Arrays.sort(numbers);
        
         for(int i : numbers)
             exist[i] = true;
             
        
        for (int i = 0; i < 10; i++) {       
            if (exist[i] != true) answer += i;
         }
        
        
        return answer;
    }
}
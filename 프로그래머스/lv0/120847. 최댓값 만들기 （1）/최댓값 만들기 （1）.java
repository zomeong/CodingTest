import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int l = numbers.length;

        Arrays.sort(numbers);
        int answer = numbers[l - 1] * numbers[l - 2];
        
        return answer;
    }
}
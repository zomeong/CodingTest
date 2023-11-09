class Solution {
    public int solution(int num) {
        int answer = 0;
        
        while(true){
            if(answer > 500) return -1;
            
            if (num == 1) break;
            else if(num % 2 == 1) num = num * 3 + 1;
            else num /= 2;
            answer++;
        }
        
        return answer;
    }
}
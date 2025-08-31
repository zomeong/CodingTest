class Solution {
    public int[] solution(int n, int k) {
        int l = n / k;
        int[] answer = new int[l];
        
        for(int i = 1; i <= l; i++){
            answer[i - 1] = i * k;
        }
        
        return answer;
    }
}
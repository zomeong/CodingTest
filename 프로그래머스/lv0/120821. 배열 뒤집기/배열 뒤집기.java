class Solution {
    public int[] solution(int[] num_list) {
        int l = num_list.length - 1;
        int[] answer = new int[l + 1];
        
        for (int i = l; i >= 0 ; i--)
            answer[l - i] = num_list[i];
        
        return answer;
    }
}
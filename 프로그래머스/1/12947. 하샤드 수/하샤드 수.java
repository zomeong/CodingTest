class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        int sum = 0;
        String l = "" + x;
        int result = x;
        int arr[] = new int[l.length()];
        
        for (int i = 0; i < l.length(); i++){
            arr[i] = x % 10;
            sum += arr[i];
            x /= 10;
        }
        
        if(result % sum == 0) answer = true;   
        
        return answer;
    }
}
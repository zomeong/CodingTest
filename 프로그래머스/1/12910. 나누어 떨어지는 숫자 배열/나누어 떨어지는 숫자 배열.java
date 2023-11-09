import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public ArrayList<Integer> solution(int[] arr, int divisor) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for(int i = 0; i < arr.length; i++)
            if(arr[i] % divisor == 0) result.add(arr[i]);
        if(result.isEmpty()) result.add(-1);
        
        Collections.sort(result);
        
        return result;
    }
}
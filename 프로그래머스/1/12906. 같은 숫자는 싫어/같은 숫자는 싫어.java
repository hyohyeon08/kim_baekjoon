import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        for(int i = 0; i < arr.length-1; i++){
            if(arr[i] != arr[i+1]){
                answer.add(arr[i]);
            }
        }
        answer.add(arr[arr.length-1]);
        return answer;
    }
}
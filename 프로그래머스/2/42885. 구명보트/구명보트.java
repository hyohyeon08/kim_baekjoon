import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int j = 0;
        Arrays.sort(people);
        for(int i = people.length-1; i >= j; i--){
            if(people[i] + people[j] <= limit){
                answer++;
                j++;
            }
            else answer++;
        }
        return answer;
    }
}
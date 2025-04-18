class Solution {
    public int solution(int n) {
        int answer = 1;
        while (true){
            if(answer * 7 / n < 1){
                answer += 1;
            }
            else{
                break;
            }
        }
        return answer;
    }
}
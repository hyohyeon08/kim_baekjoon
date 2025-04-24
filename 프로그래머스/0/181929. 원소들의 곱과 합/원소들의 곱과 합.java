class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int mul = 1;
        int fj = 0;
        for(int n : num_list){
            mul *= n;
            fj += n;
        }
        if(fj*fj > mul){
            answer = 1;
        }
        
        return answer;
    }
}
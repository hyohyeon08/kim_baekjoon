class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        int j = 0;
        int h = 0;
        
        for(int n : num_list){
            if(n%2 == 0){
                j += 1;
            }
            else{
                h += 1;
            }
        }
        answer[0] = j;
        answer[1] = h;
        return answer;
    }
}
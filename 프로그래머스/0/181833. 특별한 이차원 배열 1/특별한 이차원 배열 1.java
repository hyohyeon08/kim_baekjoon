class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int count = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(count == j) answer[i][j] = 1;
                else answer[i][j] = 0;
            }
            count += 1;
        }
        return answer;
    }
}
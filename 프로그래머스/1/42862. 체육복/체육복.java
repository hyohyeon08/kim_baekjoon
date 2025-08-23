class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] clothes = new int[n+2];
        int answer = 0;

        for(int l : lost) clothes[l] -= 1;
        for(int r : reserve) clothes[r] += 1;

        for (int i = 1; i <= n; i++) {
            if (clothes[i] == -1) {               
                if (clothes[i - 1] == 1) {           
                    clothes[i - 1] = 0;
                    clothes[i] = 0;
                } else if (clothes[i + 1] == 1) {
                    clothes[i + 1] = 0;
                    clothes[i] = 0;
                }
            }
        }
        
        for (int i = 1; i <= n; i++) {
            if (clothes[i] >= 0) answer++;
        }
        
        return answer;
    }
}
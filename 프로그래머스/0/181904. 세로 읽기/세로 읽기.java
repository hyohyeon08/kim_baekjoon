class Solution {
    public StringBuilder solution(String my_string, int m, int c) {
        Character[][] my = new Character[my_string.length() / m][m];
        int indexing = 0;
        StringBuilder answer = new StringBuilder();

        for(int i = 0; i < my_string.length() / m; i++){
            for(int j = 0; j < m; j++){
                my[i][j] = my_string.charAt(indexing);
                indexing++;
            }
        }

        for(int i = 0; i < my_string.length() / m; i++){
            answer.append(my[i][c-1]);
        }
        
        return answer;
    }
}
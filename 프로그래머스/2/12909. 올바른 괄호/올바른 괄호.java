class Solution {
    boolean solution(String s) {
        boolean answer = false;
        int stack = 0;
        for(char n: s.toCharArray()){
            stack += 1;
            if(stack == 1) continue;
            else if(n == ')'){
                stack -= 2;
            }
        }
        if(stack == 0) return true;
        return answer;
    }
}
class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        for(int i = 0; i < number.length(); i++){
            char c = number.charAt(i);
            while(k > 0 && answer.length() > 0 && answer.charAt(answer.length()-1) < c){
                k--;
                answer.deleteCharAt(answer.length()-1);
            }
            answer.append(c);
        }
        return answer.substring(0, answer.length() - k);
    }
}
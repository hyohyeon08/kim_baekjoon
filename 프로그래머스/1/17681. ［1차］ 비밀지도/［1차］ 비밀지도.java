import java.util.Arrays;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        String[] barr1 = toBinary(arr1, n);
        String[] barr2 = toBinary(arr2, n);

        for(int i = 0; i < n; i++){
            char[] ba1 = barr1[i].toCharArray();
            char[] ba2 = barr2[i].toCharArray();
            StringBuilder builder = new StringBuilder();

            for(int j = 0; j < n; j++){
                if(ba1[j] == '1' || ba2[j] == '1'){
                    builder.append("#");
                }

                else if(ba1[j] == '0' && ba2[j] == '0'){
                    builder.append(" ");
                }
            }

            answer[i] = builder.toString();
            builder.setLength(0);
        }

        return answer;
    }
    
    public static String[] toBinary(int[] arr, int n){
        return Arrays.stream(arr)
                .mapToObj(Integer::toBinaryString)
                .map(s -> String.format("%"+n+"s", s).replace(" ", "0"))
                .toArray(String[]::new);
    }
}
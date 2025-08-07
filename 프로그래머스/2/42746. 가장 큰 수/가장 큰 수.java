import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] strNumbers = Arrays.stream(numbers)
                .mapToObj(String::valueOf)
                .toArray(String[]::new);

        Arrays.sort(strNumbers, (a, b) -> (b + a).compareTo(a + b));

        if(strNumbers[0].equals("0")) return "0";
        
        StringBuilder answer = new StringBuilder();
        
        for (String strNumber : strNumbers) {
            answer.append(strNumber);
        }
        
        return answer.toString();
    }
}
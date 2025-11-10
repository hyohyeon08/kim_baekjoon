import java.util.Map;

class Solution {
    public int solution(String s) {
        Map<String, String> map = Map.of(
                "zero", "0",
                "one", "1",
                "two", "2",
                "three", "3",
                "four", "4",
                "five", "5",
                "six", "6",
                "seven", "7",
                "eight", "8",
                "nine", "9"
        );


        StringBuilder buffer = new StringBuilder();
        StringBuilder result = new StringBuilder();

        for(int i = 0; i < s.length(); i++){
            buffer.append(s.charAt(i));

            if(map.containsKey(buffer.toString())){
                result.append(map.get(buffer.toString()));
                buffer.setLength(0);
            }

            if(Character.isDigit(s.charAt(i))){
                result.append(s.charAt(i));
                buffer.setLength(0);
            }
        }

        System.out.println(result);
        return Integer.parseInt(result.toString());
    }
}
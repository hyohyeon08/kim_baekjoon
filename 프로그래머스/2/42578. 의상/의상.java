import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> cl = new HashMap<>();
        
        for (String[] clothe : clothes) {
            cl.put(clothe[1], cl.getOrDefault(clothe[1], 0) + 1);
        }

        int answer = 1;
        
        for (int count : cl.values()) {
            answer *= (count + 1); // 해당 종류에서 안 입는 경우 포함
        }
        return answer - 1; //아무 옷도 입지 안는 경우 -1
    }
}
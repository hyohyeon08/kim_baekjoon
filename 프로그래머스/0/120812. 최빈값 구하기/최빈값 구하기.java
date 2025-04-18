import java.util.HashMap;

class Solution {
    public int solution(int[] array) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num: array){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        int MaxCount = 0;
        int answer = 0;
        
        for(int key : map.keySet()){
            int count = map.get(key);
            if(MaxCount < count){
                answer = key;
                MaxCount = count;
            }
            else if(count == MaxCount){answer = -1;}
        }
        
        return answer;
    }
}
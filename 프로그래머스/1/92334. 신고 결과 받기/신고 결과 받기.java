import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, ArrayList<String>> id_report_total = new LinkedHashMap<>();//<신고 당한사람,[신고한 사람]>
        Map<String, Integer> sinGo_total = new LinkedHashMap<>(); //신고 메일 발송

        Set<String> du_report = new HashSet<>(Arrays.asList(report)); //중복 값 제거

        int[] answer = new int[id_list.length];
        
        for(String id : id_list){
            id_report_total.put(id, new ArrayList<>());
            sinGo_total.put(id, 0);
        }
        
        for (String s : du_report) { //신고 횟수 축척
            String[] sinGo = s.split(" ");

            ArrayList<String> inner = id_report_total.get(sinGo[1]);
            inner.add(sinGo[0]);
            id_report_total.put(sinGo[1], inner);
        }
        
        for (int i = 0 ; i < id_report_total.size(); i++){
            if(id_report_total.get(id_list[i]).size() >= k){
                ArrayList<String> inner = id_report_total.get(id_list[i]);
                for(String id : inner){
                    sinGo_total.put(id, sinGo_total.get(id) + 1);
                }
            }
        }
        
        for (int i = 0; i < id_list.length; i++){
            answer[i] = sinGo_total.get(id_list[i]);
        }
        
        
        return answer;
    }
}
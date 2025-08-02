import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> add = new HashMap<>();
        Map<String, Map<Integer, Integer>> music_num = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            add.put(genres[i], add.getOrDefault(genres[i], 0) + plays[i]);
            music_num.putIfAbsent(genres[i], new HashMap<>());
            music_num.get(genres[i]).put(i, plays[i]);
        }

        return add.entrySet().stream()
            .sorted((a, b) -> b.getValue() - a.getValue()) // 장르 총 재생 수 내림차순
            .flatMap(e -> music_num.get(e.getKey()).entrySet().stream()
                .sorted((a, b) -> b.getValue() - a.getValue()) // 곡 재생 수 내림차순
                .limit(2)) // 상위 2곡만
            .map(Map.Entry::getKey) // 곡 index만 추출
            .mapToInt(i -> i)
            .toArray();
    }
}

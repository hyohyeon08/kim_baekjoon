import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashSet<String> set = new HashSet<>();
        ArrayList<String> list = new ArrayList<>();

        for(int i = 0; i < n; i++){
            set.add(br.readLine());
        }
        for(int j = 0; j < m; j++){
            String text = br.readLine();
            if(set.contains(text)){
                list.add(text);
            }
        }
        System.out.println(list.size());
        list.stream()
                .sorted()
                .forEach(System.out::println);

    }
}

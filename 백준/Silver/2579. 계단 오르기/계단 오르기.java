import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] gedan = new int[n];
        int[] dp = new int[n];

        for(int i = 0; i < n; i++){
            gedan[i] = Integer.parseInt(br.readLine());
        }

        if(n <= 2){
            int sum = 0;
            for(int step : gedan){
                sum += step;
            }
            System.out.println(sum);
        }
        else{
            dp[0] = gedan[0];
            dp[1] = gedan[0] + gedan[1];
            dp[2] = Math.max(gedan[0], gedan[1]) + gedan[2];
            for(int i = 3; i < n; i++){
                dp[i] = Math.max(dp[i-3] + gedan[i-1] + gedan[i], dp[i-2] + gedan[i]);
            }
            System.out.println(dp[n-1]);
        }

    }
}

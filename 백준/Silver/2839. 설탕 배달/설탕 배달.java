import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        int ch = 0;

        while (num >= 0) {
            if (num % 5 == 0) {
                ch += num / 5;
                System.out.println(ch);
                return;
            }
            num -= 3;
            ch++;
        }

        System.out.println(-1);
    }
}

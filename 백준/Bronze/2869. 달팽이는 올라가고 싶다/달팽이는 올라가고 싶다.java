import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int V = sc.nextInt();

        System.out.println((V - B - 1) / (A - B) + 1);

    }
}

/*
A-B -> 하루에 가는 거리
마지막 날에는 미끄러지지 않음


* */
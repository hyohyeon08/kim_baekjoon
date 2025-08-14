import java.util.Arrays;
import java.util.Scanner;

public class Main {

    private static final String yes = "YES";
    private static final String no = "NO";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] num = input(sc);
        String q = judgment(num);
        System.out.println(q);
    }

    public static char[] input(Scanner sc){
        String num_string = sc.next();
        return num_string.toCharArray();
    }

    public static int arrMul(char[] num, int start, int end){
        char[] indexing_num = Arrays.copyOfRange(num, start, end);
        int sum = 1;

        for (char c : indexing_num) {
            sum *= Integer.parseInt(String.valueOf(c));
        }

        return sum;
    }


    public static String judgment(char[] num){
        for(int i = 0; i < num.length-1; i++){
            if(arrMul(num, 0, i+1) == arrMul(num, i+1, num.length)){
                return yes;
            }
        }
        return no;
    }
}
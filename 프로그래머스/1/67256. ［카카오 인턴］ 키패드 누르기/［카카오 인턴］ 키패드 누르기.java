class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();

        int leftPos = 10;  // '*'을 10으로 취급
        int rightPos = 12; // '#'을 12로 취급

        for (int num : numbers) {

            if (num == 0) num = 11;  // 편의상 0을 11로 맵핑

            if (left(num)) {
                answer.append("L");
                leftPos = num;
            } else if (right(num)) {
                answer.append("R");
                rightPos = num;
            } else {
                int leftDist = closeHand(num, leftPos);
                int rightDist = closeHand(num, rightPos);

                if (leftDist < rightDist) {
                    answer.append("L");
                    leftPos = num;
                } else if (rightDist < leftDist) {
                    answer.append("R");
                    rightPos = num;
                } else {
                    // 동일 거리 → hand 기준
                    if (hand.equals("right")) {
                        answer.append("R");
                        rightPos = num;
                    } else {
                        answer.append("L");
                        leftPos = num;
                    }
                }
            }
        }

        return answer.toString();
    }

    public static boolean left(int num) {
        return num == 1 || num == 4 || num == 7 || num == 10; // '*'은 10
    }

    public static boolean right(int num) {
        return num == 3 || num == 6 || num == 9 || num == 12; // '#'은 12
    }

    public static int closeHand(int targetNum, int startNum) {
        int d = Math.abs(targetNum - startNum);

        return (d / 3) + (d % 3);
    }
}
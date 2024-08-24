#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    unsigned long long int arr[n+1];
    arr[0] = 0;
    arr[1] = 1;
    if(n == 0){
        return 0;
    }
    else if(n == 1){
        return 1;
    }
    for(long long int i = 2; i <= n; i++){
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567;
            answer = arr[i];
            }
    return answer;
}
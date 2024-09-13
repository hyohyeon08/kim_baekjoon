function solution(my_string, is_suffix) {
    var answer = 0;
    if(my_string.length < is_suffix.length) return 0;
    for(let i = 0; i < is_suffix.length; i++){
        if(my_string[(my_string.length-1) - i] != is_suffix[(is_suffix.length-1)-i]){
            return 0
        }
        else{
            answer = 1
        }
    }
    return answer;
}
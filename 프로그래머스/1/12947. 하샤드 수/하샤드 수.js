function solution(x) {
    var answer = true;
    let score = 0
    x = x.toString()
    for(let i = 0; i < x.length; i++){
        score += parseInt(x[i])
    }
    if(parseInt(x) % score != 0) answer = false
    
    
    return answer;
}
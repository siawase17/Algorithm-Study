function solution(s) {
    var answer = [];
    let indexMap = {};
    
    for(let i = 0; i < s.length; i++){
        if (!(s[i] in indexMap)){
            answer.push(-1);
        } else {
            answer.push(i - indexMap[s[i]]);
        }
        indexMap[s[i]] = i;
    }
    return answer;
}
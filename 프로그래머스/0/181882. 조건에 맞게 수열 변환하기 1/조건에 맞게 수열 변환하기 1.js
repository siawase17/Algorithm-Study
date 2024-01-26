function solution(arr) {
    var answer = [];
    
    for (let i of arr) {
        if (i % 2 === 0 && i >= 50) {
            answer.push(i/2);
        } else if (i % 2 === 1 && i < 50) {
            answer.push(i*2);
        } else {
            answer.push(i);
        }
    }
    
    return answer;
}
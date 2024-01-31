function solution(numLog) {
    var answer = '';
    
    for (let i = 0; i < numLog.length - 1; i++) {
        let diff = numLog[i] - numLog[i + 1];

        if (diff === 1) {
            answer += 's';
        } else if (diff === -1) {
            answer += 'w';
        } else if (diff === 10) {
            answer += 'a';
        } else if (diff === -10) {
            answer += 'd';
        }
    }
    
    return answer;
}

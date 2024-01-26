function solution(s, skip, index) {
    let result = '';

    const alphabet = [];
    for (let i = 97; i <= 122; i++) {
        const letter = String.fromCharCode(i);
        if (!skip.includes(letter)) {
            alphabet.push(letter);
        }
    }

    for (let letter of s) {
        if (alphabet.includes(letter)) {
            let location = alphabet.indexOf(letter);
            let newIndex = (location + index) % alphabet.length;
            result += alphabet[newIndex];
        } else {
            result += letter; // skip에 포함된 알파벳은 그대로 결과에 추가
        }
    }

    return result;
}
function solution(babbling) {
  var answer = 0;
  let can = ["aya", "ye", "woo", "ma"];

  for (let i of babbling) {
    for (let j of can) {
      if (i.includes(j)) {
        i = i.replace(j, "X");  // 할 수 있는 단어는 X로 치환
      }
    }

    i = i.replace(/X/gi, "");  // X를 모두 공백으로 치환하고 나서
    if (i.length === 0) {  // 공백이 되면 answer에 추가
      answer += 1;
    }
  }
  return answer;
}
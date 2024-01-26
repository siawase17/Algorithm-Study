function solution(name, yearning, photo) {
    const score = new Map(name.map((name, index) => [name, yearning[index]]));
    let result = [];
    
    for (const peopleList of photo) {
        let sum = 0;

        for (const person of peopleList) {
            sum += Number(score.get(person)) || 0;
        }

        result.push(sum);
    }

    return result;
}
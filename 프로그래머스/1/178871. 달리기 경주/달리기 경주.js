function solution(players, callings) {
    const playerMap = new Map(players.map((player, index) => [player, index]));

    for (const calling of callings) {
        let index = playerMap.get(calling);
        [players[index - 1], players[index]] = [players[index], players[index - 1]];
        playerMap.set(players[index], index);
        playerMap.set(players[index - 1], index - 1);
    }

    return players;
}

